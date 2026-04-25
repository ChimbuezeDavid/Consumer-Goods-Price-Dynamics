# app/models.py
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
from pathlib import Path
from datetime import datetime
import statsmodels.api as sm
import warnings
import streamlit as st

warnings.filterwarnings('ignore')

class ForecastEngine:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.models_dir = self.base_dir / "models"
        self.data_path = self.base_dir / "data" / "merged_macro_cpi_2000_2026.csv"
        
        self.base_models = {"sarimax": {}, "rf": {}, "lstm": {}, "scalers": {}}
        self.meta_models = {}
        self.load_errors = []
        
        self._load_all_models()
        self._load_recent_data()

    def _load_all_models(self):
        targets = ["food_mom", "transport_mom", "clothing_mom"]
        display_names = {"food_mom": "Food", "transport_mom": "Transport", "clothing_mom": "Clothing And Footwear"}
        
        for t in targets:
            dn = display_names[t]
            
            # Load SARIMAX
            try:
                p = self.models_dir / f"sarimax_{t}.pkl"
                if p.exists():
                    with open(p, "rb") as f:
                        self.base_models["sarimax"][dn] = pickle.load(f)
                else:
                    self.load_errors.append(f"Missing SARIMAX: {p.name}")
            except Exception as e:
                self.load_errors.append(f"Error loading SARIMAX {t}: {str(e)}")
            
            # Load RF
            try:
                p = self.models_dir / f"randomforest_{t}_tuned.pkl"
                if p.exists():
                    with open(p, "rb") as f:
                        self.base_models["rf"][dn] = pickle.load(f)
                else:
                    self.load_errors.append(f"Missing RF: {p.name}")
            except Exception as e:
                self.load_errors.append(f"Error loading RF {t}: {str(e)}")
            
            # Load LSTM
            try:
                p_model = self.models_dir / f"lstm_{t}_final.keras"
                p_scaler = self.models_dir / f"lstm_scaler_{t}.pkl"
                if p_model.exists() and p_scaler.exists():
                    self.base_models["lstm"][dn] = tf.keras.models.load_model(p_model)
                    with open(p_scaler, "rb") as f:
                        self.base_models["scalers"][dn] = pickle.load(f)
                else:
                    self.load_errors.append(f"Missing LSTM or Scaler for {t}")
            except Exception as e:
                self.load_errors.append(f"Error loading LSTM {t}: {str(e)}")
            
            # Load Stacked (Meta)
            try:
                p = self.models_dir / f"stacked_final_{t}.pkl"
                if p.exists():
                    with open(p, "rb") as f:
                        self.meta_models[dn] = pickle.load(f)
                else:
                    self.load_errors.append(f"Missing Meta Model: {p.name}")
            except Exception as e:
                self.load_errors.append(f"Error loading Meta {t}: {str(e)}")

    def _load_recent_data(self):
        try:
            if not self.data_path.exists():
                self.load_errors.append(f"Data file not found: {self.data_path}")
                self.recent_df = pd.DataFrame()
                return

            df = pd.read_csv(self.data_path)
            df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce')
            df = df.sort_values('date').reset_index(drop=True)
            df['all_items_mom'] = df['All Items'].pct_change() * 100
            df['food_mom'] = df['Food'].pct_change() * 100
            df['transport_mom'] = df['Transport'].pct_change() * 100
            df['clothing_mom'] = df['Clothing And Footwear'].pct_change() * 100
            self.recent_df = df.tail(10).copy()
        except Exception as e:
            self.load_errors.append(f"Data processing error: {str(e)}")
            self.recent_df = pd.DataFrame()

    def _create_features(self, df):
        features = ['exchange_rate', 'oil_price', 'all_items_mom']
        lags = [1, 2]
        windows = [3]
        for col in features + ['food_mom', 'transport_mom', 'clothing_mom']:
            for lag in lags:
                df[f'{col}_lag_{lag}'] = df[col].shift(lag)
        for col in features:
            for window in windows:
                df[f'{col}_roll_mean_{window}'] = df[col].rolling(window=window).mean()
                df[f'{col}_roll_std_{window}'] = df[col].rolling(window=window).std()
        df['month'] = df['date'].dt.month
        df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
        df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
        df['post_covid'] = (df['date'] >= '2020-03-01').astype(int)
        df['post_2023_deval'] = (df['date'] >= '2023-06-01').astype(int)
        return df

    def predict(self, inflation_rate: float, exchange_rate: float, oil_price: float, horizon: int = 12):
        categories = ["Food", "Transport", "Clothing And Footwear"]
        col_map = {"Food": "food_mom", "Transport": "transport_mom", "Clothing And Footwear": "clothing_mom"}
        
        sim_df = self.recent_df.copy()
        last_date = sim_df['date'].max()
        
        all_results = {cat: [] for cat in categories}
        
        for i in range(horizon):
            next_date = last_date + pd.DateOffset(months=1)
            new_row = {
                'date': next_date, 'exchange_rate': exchange_rate, 'oil_price': oil_price,
                'all_items_mom': inflation_rate, 'All Items': 0, 'Food': 0, 'Transport': 0,
                'Clothing And Footwear': 0, 'food_mom': 0, 'transport_mom': 0, 'clothing_mom': 0
            }
            sim_df = pd.concat([sim_df, pd.DataFrame([new_row])], ignore_index=True)
            temp_df = self._create_features(sim_df.copy())
            current_features_df = temp_df.tail(1)
            
            targets = ['food_mom', 'transport_mom', 'clothing_mom']
            feature_cols = [col for col in temp_df.columns if col not in ['date'] + targets]
            X = current_features_df[feature_cols]
            
            for category in categories:
                if category not in self.meta_models: continue
                
                try: sar_pred = self.base_models["sarimax"][category].forecast(steps=1, exog=X).values[0]
                except: sar_pred = 0
                
                try: rf_pred = self.base_models["rf"][category].predict(X)[0]
                except: rf_pred = 0
                
                try:
                    scaler = self.base_models["scalers"][category]
                    model_lstm = self.base_models["lstm"][category]
                    X_scaled = scaler.transform(temp_df[feature_cols].tail(2))
                    X_seq = np.array([X_scaled])
                    lstm_pred = model_lstm.predict(X_seq, verbose=0).flatten()[0]
                except: lstm_pred = 0
                
                meta_pred = self.meta_models[category].predict(np.array([[sar_pred, rf_pred, lstm_pred]]))[0]
                
                # Add randomness to account for unobserved factors
                noise = np.random.normal(0, abs(meta_pred) * 0.08 + 0.15)
                meta_pred += noise
                
                all_results[category].append(float(meta_pred))
                sim_df.loc[sim_df.index[-1], col_map[category]] = meta_pred
            
            last_date = next_date
            
        return {cat: [round(p, 2) for p in preds] for cat, preds in all_results.items()}

# Initialize engine
forecast_engine = ForecastEngine()