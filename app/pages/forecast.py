# app/pages/forecast.py
"""
NairaPulse AI - Clean Forecast Terminal
Simplified UI with better spacing, removed presets, improved chart color.
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

def interpret_forecast(avg_mom, category):
    """Generate simple interpretation of forecast."""
    if avg_mom > 3:
        severity = "🔴 High Inflation"
        desc = f"Prices rising significantly"
    elif avg_mom > 1.5:
        severity = "🟡 Moderate Inflation"
        desc = f"Normal price increases"
    elif avg_mom > 0:
        severity = "🟢 Mild Inflation"
        desc = f"Gradual price rise"
    elif avg_mom > -1:
        severity = "🔵 Stable"
        desc = f"Minimal price change"
    else:
        severity = "🟣 Deflation"
        desc = f"Prices falling"
    
    return severity, desc

def show_forecast():
    render_hero(
        title="Forecast Terminal",
        subtitle="Configure economic parameters and generate month-over-month price forecasts."
    )

    # Sidebar Parameters - Cleaner labels
    st.sidebar.markdown("### Configure Parameters")
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    horizon = st.sidebar.slider(
        "Forecast Horizon (Months)", 
        3, 24, 12,
        help="Number of months to forecast"
    )
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    inflation_rate = st.sidebar.slider(
        "Headline Inflation (MoM %)", 
        5.0, 60.0, 28.0, 0.5,
        help="Overall monthly inflation rate"
    )
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    exchange_rate = st.sidebar.number_input(
        "Exchange Rate (₦ per USD)", 
        300.0, 5000.0, 1356.89, 1.0,
        help="Official exchange rate"
    )
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    oil_price = st.sidebar.number_input(
        "Brent Crude ($/barrel)", 
        30.0, 200.0, 95.0, 0.5,
        help="Global oil price benchmark"
    )
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    category = st.sidebar.selectbox(
        "Focus Category", 
        ["Food", "Transport", "Clothing And Footwear"]
    )

    st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

    # Run Forecast Button
    if st.sidebar.button("🚀 RUN FORECAST", use_container_width=True, type="primary"):
        with st.spinner("Running forecast engine..."):
            predictions = forecast_engine.predict(
                inflation_rate=inflation_rate,
                exchange_rate=exchange_rate,
                oil_price=oil_price,
                horizon=horizon
            )
        
        result = predictions.get(category, [0.0] * horizon)
        avg_mom = sum(result) / len(result)
        peak_mom = max(result)
        min_mom = min(result)

        # Simple Interpretation
        severity, desc = interpret_forecast(avg_mom, category)
        
        st.markdown(f"""
        <div style="background:var(--np-surface); padding:1.5rem; border-radius:12px; 
                    border-left:4px solid var(--np-accent); margin-bottom:2rem;">
            <div style="font-size:1.3rem; font-weight:700; margin-bottom:0.5rem;">{severity}</div>
            <div style="color:var(--np-muted);">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

        # Key Metrics - More spacing
        st.markdown("<br>", unsafe_allow_html=True)
        
        avg_color = "var(--np-success)" if avg_mom > 0 else "var(--np-danger)" if avg_mom < 0 else "var(--np-primary)"
        peak_color = "var(--np-success)" if peak_mom > 0 else "var(--np-danger)" if peak_mom < 0 else "var(--np-primary)"
        min_color = "var(--np-success)" if min_mom > 0 else "var(--np-danger)" if min_mom < 0 else "var(--np-primary)"

        c1, c2, c3, c4 = st.columns(4, gap="large")
        with c1:
            render_metric_card("Current Index", f"{LAST_KNOWN_CPI.get(category, 500.0):,.1f}")
        with c2:
            render_metric_card("Avg. MoM", f"{avg_mom:+.2f}%", color=avg_color)
        with c3:
            render_metric_card("Peak MoM", f"{peak_mom:+.2f}%", color=peak_color)
        with c4:
            render_metric_card("Lowest MoM", f"{min_mom:+.2f}%", color=min_color)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Chart and Table - Better layout
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

        # Chart - Full width
        st.markdown("**Projected Price Trend**")
        from app.colors import get_theme
        theme = get_theme(st.session_state.dark_mode)
        fig = create_forecast_chart(dates, result, category, theme)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Table below chart
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.markdown("**Monthly Forecast Table**")
            styled_df = forecast_df.style.format({
                "MoM Change (%)": "{:+.2f}%",
                "Implied Index": "{:,.2f}"
            }).map(color_mom, subset=["MoM Change (%)"])
            st.dataframe(styled_df, use_container_width=True, hide_index=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Cumulative Impact - Cleaner
        cumulative_change = ((implied_indices[-1] / LAST_KNOWN_CPI.get(category, 500.0)) - 1) * 100
        
        col_impact1, col_impact2, col_impact3 = st.columns([1, 2, 1])
        with col_impact2:
            st.markdown(f"""
            <div style="background:var(--np-surface); padding:1.8rem; border-radius:12px; text-align:center; border:1px solid var(--np-border);">
                <div style="color:var(--np-muted); font-size:0.95rem; margin-bottom:0.8rem;">
                    Total Impact Over {horizon} Months
                </div>
                <div style="font-size:2.5rem; font-weight:800; color:{'var(--np-success)' if cumulative_change > 0 else 'var(--np-danger)'};">
                    {cumulative_change:+.1f}%
                </div>
                <div style="color:var(--np-muted); font-size:0.9rem; margin-top:0.8rem;">
                    ₦100 today → ₦{100 * (1 + cumulative_change/100):.2f} in {horizon} months
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Download Section
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
        with col_dl2:
            csv = forecast_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Forecast (CSV)", 
                csv, 
                f"nairapulse_{category.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv", 
                "text/csv", 
                use_container_width=True
            )
        
    else:
        # Initial State - Simplified
        st.markdown("""
        <div style="text-align:center; padding:5rem 2rem; background:var(--np-surface); 
                    border-radius:16px; border:2px dashed var(--np-border);">
            <div style="font-size:4rem; margin-bottom:1.5rem;">📊</div>
            <h3 style="color:var(--np-primary); margin-bottom:1.5rem;">
                Configure Parameters & Run Forecast
            </h3>
            <p style="color:var(--np-muted); font-size:1.15rem; max-width:600px; margin:0 auto;">
                Use the sidebar to set your assumptions, then click 
                <strong>"RUN FORECAST"</strong> to generate predictions.
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_forecast()