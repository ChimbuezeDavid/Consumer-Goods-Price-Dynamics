# pages/forecast.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from app.models import forecast_engine
from app.utils import create_forecast_chart
from app.config import LAST_KNOWN_CPI, THEME

def color_mom(val):
    """Color coding for MoM changes"""
    try:
        num = float(val.replace('%', ''))
        if num < 0:
            return f'color: {THEME["danger"]}; font-weight: 700;'
        elif num > 0:
            return f'color: {THEME["success"]}; font-weight: 700;'
    except: pass
    return ''

def show_forecast():
    # Check for engine loading errors
    if forecast_engine.load_errors:
        with st.expander("⚠️ System Alert", expanded=False):
            for err in forecast_engine.load_errors:
                st.warning(err)

    # Sidebar
    with st.sidebar:
        st.markdown(f"### <span style='color: white'>🎛️ Simulation Controls</span>", unsafe_allow_html=True)
        
        horizon = st.slider("Forecast Horizon (Months)", 1, 24, 6)
        
        st.markdown("---")
        # Aligning with Headline Inflation as requested by user
        headline_inflation = st.slider("Headline Inflation (%)", 0.0, 60.0, 15.38, 0.01)
        exchange_rate = st.number_input("Official FX Rate (₦/$)", 100.0, 5000.0, 1351.35, 0.01)
        oil_price = st.number_input("Brent Crude Oil ($/bbl)", 10.0, 300.0, 105.33, 0.01)

        st.markdown("---")
        generate = st.button("🚀 RUN SIMULATION", type="primary", use_container_width=True)

    if generate:
        with st.spinner("Calculating Stacked Pulse..."):
            # Map headline inflation back to the MoM model parameter if needed, 
            # or use directly if model is adjusted.
            predictions = forecast_engine.predict(
                inflation_rate=headline_inflation / 12, # Rough conversion for MoM model input
                exchange_rate=exchange_rate,
                oil_price=oil_price,
                horizon=horizon
            )
        
        if predictions:
            # Metrics Row - Cleaner UI
            cols = st.columns(3)
            cats = ["Food", "Transport", "Clothing And Footwear"]
            icons = ["🥘", "🚗", "👕"]
            baselines = [2.5, 1.8, 1.2]
            
            for i, cat in enumerate(cats):
                val = sum(predictions[cat]) / len(predictions[cat])
                cols[i].metric(f"{icons[i]} {cat}", f"{val:.2f}%", f"{val - baselines[i]:+.1f}%", delta_color="inverse")

            # Main Dashboard Body
            tab1, tab2 = st.tabs(["📈 Market Visuals", "📋 Tabular Pulse"])
            
            dates = pd.date_range(datetime.now() + timedelta(days=30), periods=horizon, freq='M')
            
            with tab1:
                # Top Level Chart
                st.plotly_chart(create_forecast_chart(dates, predictions['Food'], "Food Price Forecast"), use_container_width=True)
                
                # Side by Side Charts
                c_a, c_b = st.columns(2)
                with c_a:
                    st.plotly_chart(create_forecast_chart(dates, predictions['Transport'], "Transport"), use_container_width=True)
                with c_b:
                    st.plotly_chart(create_forecast_chart(dates, predictions['Clothing And Footwear'], "Clothing"), use_container_width=True)
            
            with tab2:
                df = pd.DataFrame({
                    "Date": dates.strftime("%b %Y"),
                    "Food": [f"{p:+.2f}%" for p in predictions['Food']],
                    "Transport": [f"{p:+.2f}%" for p in predictions['Transport']],
                    "Clothing": [f"{p:+.2f}%" for p in predictions['Clothing And Footwear']]
                })
                st.dataframe(df.style.applymap(color_mom, subset=["Food", "Transport", "Clothing"]), use_container_width=True, hide_index=True)

    else:
        st.markdown(f"""
            <div style="text-align: center; padding: 5rem; color: #E2E8F0;">
                <div style="font-size: 4rem; margin-bottom: 1.5rem; opacity: 0.3;">📉</div>
                <h2 style="font-weight: 800; color: white;">Ready to simulate custom scenarios.</h2>
                <p style="opacity: 0.7;">Adjust the parameters in the sidebar and initiate the forecast.</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_forecast()