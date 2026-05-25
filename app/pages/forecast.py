# app/pages/forecast.py
"""
NairaPulse AI - Forecast Terminal
Clean forecast interface with IcoFont icons. No emojis.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from app.models import forecast_engine
from app.utils import create_forecast_chart
from app.config import LAST_KNOWN_CPI
from app.ui_components import render_hero, render_section_header, render_metric_card


def color_mom(val):
    """Colour month-over-month percentage values in the summary table."""
    from app.colors import get_theme
    theme = get_theme(st.session_state.dark_mode)
    try:
        num = float(val)
        if num > 0:
            return f'color: {theme["success"]}; font-weight: 700;'
        elif num < 0:
            return f'color: {theme["danger"]}; font-weight: 700;'
    except Exception:
        pass
    return ''


def interpret_forecast(avg_mom, category):
    """Return a severity label and plain-English description of the forecast outlook."""
    if avg_mom > 3:
        severity = "High Inflationary Pressure"
        icon_class = "icofont-warning-alt"
        color = "#EF4444"
        desc = "Prices are projected to rise at an above-average rate. Consider near-term procurement and cost hedging strategies."
    elif avg_mom > 1.5:
        severity = "Moderate Inflationary Pressure"
        icon_class = "icofont-info-circle"
        color = "#F59E0B"
        desc = "Price increases are within the normal historical range. Monitor closely for supply-side developments."
    elif avg_mom > 0:
        severity = "Mild Inflationary Pressure"
        icon_class = "icofont-check-circled"
        color = "#10B981"
        desc = "Gradual, low-level price increases are expected. Conditions appear broadly stable."
    elif avg_mom > -1:
        severity = "Price Stability"
        icon_class = "icofont-check-circled"
        color = "#0F172A"
        desc = "Prices are projected to remain broadly flat. Minimal inflationary or deflationary risk in this category."
    else:
        severity = "Deflationary Signal"
        icon_class = "icofont-minus-circle"
        color = "#6366F1"
        desc = "Prices are projected to decline on average. This may reflect demand contraction or FX appreciation."

    return severity, icon_class, color, desc


def show_forecast():
    render_hero(
        title="Forecast Terminal",
        subtitle="Configure macroeconomic assumptions and generate probabilistic month-over-month price forecasts for key Nigerian consumer goods categories."
    )

    # Sidebar Parameters
    st.sidebar.markdown("### Forecast Parameters")
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    horizon = st.sidebar.slider(
        "Forecast Horizon (Months)",
        3, 24, 12,
        help="Number of calendar months to project forward from the current date."
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    inflation_rate = st.sidebar.slider(
        "Headline Inflation (Month-over-Month %)",
        5.0, 60.0, 28.0, 0.5,
        help="The overall consumer price inflation rate expressed as a month-over-month percentage change."
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    exchange_rate = st.sidebar.number_input(
        "USD/NGN Exchange Rate (Naira per Dollar)",
        300.0, 5000.0, 1356.89, 1.0,
        help="The official CBN spot exchange rate. Higher values reflect naira depreciation."
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    oil_price = st.sidebar.number_input(
        "Brent Crude Oil Price (USD per barrel)",
        30.0, 200.0, 95.0, 0.5,
        help="International benchmark crude oil price. A key driver of domestic fuel and transport costs."
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    category = st.sidebar.selectbox(
        "Target Category",
        ["Food", "Transport", "Clothing And Footwear"],
        help="Select the consumer goods category to forecast."
    )

    st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

    if st.sidebar.button("RUN FORECAST", use_container_width=True, type="primary"):
        with st.spinner("Running ensemble forecast engine..."):
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

        severity, icon_class, color, desc = interpret_forecast(avg_mom, category)

        st.markdown(f"""
        <div style="background:var(--np-surface); padding:1.5rem 2rem; border-radius:12px; 
                    border-left:4px solid {color}; margin-bottom:2rem;">
            <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.4rem;">
                <i class="{icon_class}" style="font-size:1.4rem; color:{color};"></i>
                <span style="font-size:1.2rem; font-weight:700; color:{color};">{severity}</span>
            </div>
            <div style="color:var(--np-muted); font-size:0.95rem; line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        avg_color = "var(--np-success)" if avg_mom > 0 else "var(--np-danger)" if avg_mom < 0 else "var(--np-primary)"
        peak_color = "var(--np-success)" if peak_mom > 0 else "var(--np-danger)" if peak_mom < 0 else "var(--np-primary)"
        min_color = "var(--np-success)" if min_mom > 0 else "var(--np-danger)" if min_mom < 0 else "var(--np-primary)"

        c1, c2, c3, c4 = st.columns(4, gap="large")
        with c1:
            render_metric_card("Base Index Level", f"{LAST_KNOWN_CPI.get(category, 500.0):,.1f}")
        with c2:
            render_metric_card("Avg. Monthly Change", f"{avg_mom:+.2f}%", color=avg_color)
        with c3:
            render_metric_card("Peak Monthly Change", f"{peak_mom:+.2f}%", color=peak_color)
        with c4:
            render_metric_card("Minimum Monthly Change", f"{min_mom:+.2f}%", color=min_color)

        st.markdown("<br>", unsafe_allow_html=True)

        dates = pd.date_range(datetime.now(), periods=horizon, freq='ME')

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

        cumulative_change = ((implied_indices[-1] / LAST_KNOWN_CPI.get(category, 500.0)) - 1) * 100

        col_impact1, col_impact2, col_impact3 = st.columns([1, 2, 1])
        with col_impact2:
            impact_color = 'var(--np-success)' if cumulative_change > 0 else 'var(--np-danger)'
            st.markdown(f"""
            <div style="background:var(--np-surface); padding:1.8rem; border-radius:12px; 
                        text-align:center; border:1px solid var(--np-border);">
                <div style="color:var(--np-muted); font-size:0.95rem; margin-bottom:0.8rem;">
                    Cumulative Price Change Over {horizon} Months
                </div>
                <div style="font-size:2.5rem; font-weight:800; color:{impact_color};">
                    {cumulative_change:+.1f}%
                </div>
                <div style="color:var(--np-muted); font-size:0.9rem; margin-top:0.8rem;">
                    &#8358;100 in purchasing power today &rarr; &#8358;{100 * (1 + cumulative_change/100):.2f} equivalent in {horizon} months
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Table
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.markdown("**Monthly Forecast Table**")
            styled_df = forecast_df.style.format({
                "MoM Change (%)": "{:+.2f}%",
                "Implied Index": "{:,.2f}"
            }).map(color_mom, subset=["MoM Change (%)"])
            st.dataframe(styled_df, use_container_width=True, hide_index=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Chart
        st.markdown("**Projected Price Trend**")
        from app.colors import get_theme
        theme = get_theme(st.session_state.dark_mode)
        fig = create_forecast_chart(dates, result, category, theme)
        st.plotly_chart(fig, use_container_width=True)

        # Download
        st.markdown("<br>", unsafe_allow_html=True)
        col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
        with col_dl2:
            csv = forecast_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "Download Forecast Data (CSV)",
                csv,
                f"nairapulse_{category.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
                "text/csv",
                use_container_width=True
            )

    else:
        st.markdown("""
        <div style="text-align:center; padding:5rem 2rem; background:var(--np-surface); 
                    border-radius:16px; border:2px dashed var(--np-border);">
            <i class="icofont-chart-bar-graph np-icon-primary" style="font-size:4rem; display:block; margin-bottom:1.5rem;"></i>
            <h3 style="color:var(--np-primary); margin-bottom:1.5rem;">
                Configure Parameters &amp; Run Forecast
            </h3>
            <p style="color:var(--np-muted); font-size:1.1rem; max-width:600px; margin:0 auto; line-height:1.7;">
                Use the sidebar controls to set your macroeconomic assumptions: exchange rate, 
                oil price, headline inflation. Then click <strong>Run Forecast</strong> to generate 
                a detailed month-by-month price outlook.
            </p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    show_forecast()