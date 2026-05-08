# pages/forecast.py
"""
NairaPulse AI - Forecast Terminal
Green/Red only for MoM values. Consistent chart line. Improved buttons.
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from app.models import forecast_engine
from app.utils import create_forecast_chart
from app.config import LAST_KNOWN_CPI
from app.ui_components import render_hero, render_section_header, render_metric_card

def color_mom(val):
    """Green/Red ONLY for MoM percentage values in the table."""
    from app.colors import get_theme
    theme = get_theme(st.session_state.dark_mode)
    
    try:
        num = float(val)
        if num > 0:
            return f'color: {theme["success"]}; font-weight: 700;'
        elif num < 0:
            return f'color: {theme["danger"]}; font-weight: 700;'
    except:
        pass
    return ''



def show_forecast():
    render_hero(
        title="Forecast Terminal",
        subtitle="Configure macroeconomic variables and generate realistic month-over-month price projections."
    )

    st.sidebar.markdown("### Simulation Parameters")
    
    horizon = st.sidebar.slider("Forecast Horizon (Months)", 3, 24, 12)
    inflation_rate = st.sidebar.slider("Headline Inflation (MoM %)", 5.0, 60.0, 28.0, 0.5)
    exchange_rate = st.sidebar.number_input("Official Exchange Rate (₦ per USD)", 300.0, 5000.0, 1356.89, 1.0)
    oil_price = st.sidebar.number_input("Brent Crude Oil ($/barrel)", 30.0, 200.0, 95.0, 0.5)
    category = st.sidebar.selectbox("Focus Category", ["Food", "Transport", "Clothing And Footwear"])

    if st.sidebar.button("🚀 RUN FORECAST", use_container_width=True, type="primary"):
        with st.spinner("Running stacked ensemble model..."):
            predictions = forecast_engine.predict(
                inflation_rate=inflation_rate,
                exchange_rate=exchange_rate,
                oil_price=oil_price,
                horizon=horizon
            )
        
        result = predictions.get(category, [0.0] * horizon)
        avg_mom = sum(result) / len(result)
        peak_mom = max(result)

        render_section_header("📈", f"{category} Price Outlook")

        avg_color = "var(--np-success)" if avg_mom > 0 else "var(--np-danger)" if avg_mom < 0 else "var(--np-primary)"
        peak_color = "var(--np-success)" if peak_mom > 0 else "var(--np-danger)" if peak_mom < 0 else "var(--np-primary)"

        c1, c2, c3 = st.columns(3, gap="medium")
        with c1:
            render_metric_card("Current Index", f"{LAST_KNOWN_CPI.get(category, 500.0):,.1f}")
        with c2:
            render_metric_card("Avg. MoM Change", f"{avg_mom:+.2f}%", color=avg_color)
        with c3:
            render_metric_card("Peak MoM", f"{peak_mom:+.2f}%", color=peak_color)

        dates = pd.date_range(datetime.now() + timedelta(days=30), periods=horizon, freq='ME')
        
        current_index = LAST_KNOWN_CPI.get(category, 500.0)
        implied_indices = []
        for mom in result:
            current_index *= (1 + mom / 100)
            implied_indices.append(round(current_index, 2))

        forecast_df = pd.DataFrame({
            "Month": dates.strftime("%b %Y"),
            "MoM Change (%)": result,
            "Implied Index": implied_indices
        })

        left, right = st.columns([1.75, 1], gap="large")
        
        with left:
            st.markdown("**Projected Price Trend**")
            from app.colors import get_theme
            theme = get_theme(st.session_state.dark_mode)
            fig = create_forecast_chart(dates, result, category, theme)
            st.plotly_chart(fig, use_container_width=True)
        
        with right:
            st.markdown("**Monthly Forecast Table**")
            styled_df = forecast_df.style.format({
                "MoM Change (%)": "{:+.2f}%",
                "Implied Index": "{:,.2f}"
            }).map(color_mom, subset=["MoM Change (%)"])
            st.dataframe(styled_df, use_container_width=True, hide_index=True)


        csv = forecast_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Forecast (CSV)", csv, 
                         f"nairapulse_{category.lower().replace(' ', '_')}_forecast.csv", 
                         "text/csv", use_container_width=True)
        
    else:
        st.info("👈 Use the sidebar to configure parameters and run the simulation.", icon="ℹ️")

if __name__ == "__main__":
    show_forecast()