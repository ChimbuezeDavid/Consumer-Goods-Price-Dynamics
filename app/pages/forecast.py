import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from app.models import generate_future_forecast
from app.utils import create_forecast_chart
from app.config import LAST_KNOWN_CPI

def show_forecast():
    st.title("📈 Forecast Month-on-Month Price Shifts")
    st.caption("Stacked Ensemble Model • SARIMAX + Random Forest + LSTM + XGBoost")

    st.sidebar.header("Your Scenario")
    
    horizon = st.sidebar.slider("Forecast Horizon (months)", 3, 24, 12)
    inflation = st.sidebar.slider("Inflation Rate (%)", 5.0, 60.0, 28.0, 0.5)
    exchange_rate = st.sidebar.number_input("Exchange Rate (NGN/USD)", 300.0, 3000.0, 1356.89, 10.0)
    oil_price = st.sidebar.number_input("Crude Oil Price (USD/barrel)", 30.0, 200.0, 95.20, 1.0)
    
    category = st.sidebar.selectbox(
        "Select CPI Category",
        list(LAST_KNOWN_CPI.keys())
    )

    if st.sidebar.button("🚀 Generate Forecast", type="primary"):
        with st.spinner("Running stacked ensemble model..."):
            forecast_df, error = generate_future_forecast(
                category, horizon, inflation, exchange_rate, oil_price
            )
            
            if error:
                st.error(error)
            else:
                st.success(f"✅ Forecast generated for **{category}**")

                # Summary Metrics - Balanced
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Current CPI Index", f"{LAST_KNOWN_CPI.get(category, 500.0):.1f}")
                with col2:
                    avg_mom = forecast_df["Predicted_MoM_pct"].mean()
                    st.metric("Average MoM Change", f"{avg_mom:.2f}%")
                with col3:
                    st.metric("Forecast Horizon", f"{horizon} months")

                # Forecast Table - Dynamic width, clean formatting
                st.subheader("Forecast Results")
                
                display_df = forecast_df[["Date", "Predicted_MoM_pct", "Implied_CPI_Index"]].copy()
                display_df = display_df.rename(columns={
                    "Predicted_MoM_pct": "MoM % Change",
                    "Implied_CPI_Index": "Implied New CPI Index"
                })
                
                # Clean styling with dynamic fit
                styled = display_df.style.format({
                    "MoM % Change": "{:+.2f}%",
                    "Implied New CPI Index": "{:.2f}"
                }).apply(lambda row: ['color: #00cc66; font-weight: bold' if row["MoM % Change"] >= 0 
                                    else 'color: #ff4d4d; font-weight: bold' for _ in row], axis=1)

                st.dataframe(
                    styled,
                    use_container_width=True,
                    hide_index=True,
                    height=420
                )

                # Improved Chart (existing one, but cleaner)
                st.subheader("Visualization")
                fig = create_forecast_chart(
                    pd.to_datetime(forecast_df["Date"], format="%b %Y"),
                    forecast_df["Predicted_MoM_pct"],
                    category
                )
                st.plotly_chart(fig, use_container_width=True)

                # Download
                csv = forecast_df.to_csv(index=False)
                st.download_button(
                    "📥 Download Forecast CSV",
                    data=csv,
                    file_name=f"forecast_{category.replace(' ', '_')}.csv",
                    mime="text/csv"
                )