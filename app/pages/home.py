# app/pages/home.py
"""
NairaPulse AI - Home Page
Professional landing page with IcoFont icons and publication-quality copy.
"""

import streamlit as st
from app.ui_components import render_hero, render_section_header

def show_home():
    """Landing page with clean, spacious layout and professional copy."""
    render_hero(
        title="NairaPulse AI",
        subtitle="An ensemble machine learning system for forecasting consumer goods price dynamics in Nigeria, built on 25 years of CPI data, macroeconomic indicators, and rigorous statistical modelling."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Introduction
    col_a, col_b = st.columns([2, 1], gap="large")

    with col_a:
        st.markdown("""
        ### What is NairaPulse AI?

        NairaPulse AI is an open research platform that applies stacked ensemble learning to 
        forecast **month-over-month price changes** in three critical Nigerian consumer goods categories:

        - **Food** -- the single largest household expenditure, sensitive to harvest cycles and exchange rate shocks
        - **Transport** -- tightly linked to global crude oil prices and domestic fuel subsidy policies
        - **Clothing & Footwear** -- highly import-dependent, tracking naira depreciation in near real-time

        Together, these three categories represent over **70% of Nigerian household spending**. 
        Accurate short-to-medium-term forecasts of these categories directly informs household 
        budgeting, procurement planning, academic research, and macroeconomic policy analysis.

        The system is designed to be accessible to researchers, policymakers, and practitioners 
        both within Nigeria and internationally.
        """)

    with col_b:
        st.markdown(f"""
        <div class="np-card" style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); color:white;">
            <h4 style="margin-top:0; color:white; font-size:1rem; letter-spacing:0.06em; opacity:0.85;">
                LATEST MACRO INDICATORS
            </h4>
            <div style="font-size:2.4rem; font-weight:800; margin:1rem 0; letter-spacing:-0.03em;">15.38%</div>
            <div style="opacity:0.9; margin-bottom:1.5rem; font-size:0.95rem;">Headline Inflation (Month-over-Month)</div>
            <hr style="margin:1.5rem 0; border:0; border-top:1px solid rgba(255,255,255,0.3);">
            <div style="opacity:0.9; line-height:2; font-size:0.95rem;">
                <strong>₦1,351 / USD</strong> &nbsp; Exchange Rate<br>
                <strong>$105 / barrel</strong> &nbsp; Brent Crude
            </div>
            <div style="margin-top:1rem; font-size:0.78rem; opacity:0.65;">
                Source: CBN / NBS, Feb 2026
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Categories
    render_section_header(
        '<i class="icofont-chart-bar-graph np-icon-primary"></i>',
        "Forecast Categories"
    )

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        st.markdown("""
        <div class="np-card" style="text-align:center; height:100%;">
            <div style="margin-bottom:1.2rem;">
                <i class="icofont-food-basket np-icon-primary" style="font-size:3rem;"></i>
            </div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Food</h3>
            <div style="color:var(--np-muted); line-height:1.9; font-size:0.95rem;">
                Largest CPI component<br>
                Driven by FX &amp; harvest cycles<br>
                Typical MoM range: &minus;3% to +8%<br>
                <em style="font-size:0.85rem;">~50% of household budgets</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="np-card" style="text-align:center; height:100%;">
            <div style="margin-bottom:1.2rem;">
                <i class="icofont-car np-icon-primary" style="font-size:3rem;"></i>
            </div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Transport</h3>
            <div style="color:var(--np-muted); line-height:1.9; font-size:0.95rem;">
                Energy price channel<br>
                Tracks global crude oil benchmarks<br>
                Typical MoM range: &minus;2% to +6%<br>
                <em style="font-size:0.85rem;">~12% of household budgets</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="np-card" style="text-align:center; height:100%;">
            <div style="margin-bottom:1.2rem;">
                <i class="icofont-safety np-icon-primary" style="font-size:3rem;"></i>
            </div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Clothing &amp; Footwear</h3>
            <div style="color:var(--np-muted); line-height:1.9; font-size:0.95rem;">
                Import-dependent sector<br>
                Follows naira exchange rate<br>
                Typical MoM range: &minus;1% to +4%<br>
                <em style="font-size:0.85rem;">~6% of household budgets</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Forecasting Approach
    render_section_header(
        '<i class="icofont-ui-settings np-icon-primary"></i>',
        "Forecasting Architecture"
    )

    st.markdown("""
    NairaPulse AI uses a **stacked generalization** (meta-learning) architecture. Three 
    specialised base models, each extracting a different signal from the data, are combined 
    by a trained meta-learner that learns the optimal weighted combination:
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div class="np-card" style="text-align:center; padding:1.8rem;">
            <div style="margin-bottom:0.8rem;">
                <i class="icofont-chart-line np-icon-primary" style="font-size:2.2rem;"></i>
            </div>
            <h4 style="color:var(--np-primary); margin-bottom:0.8rem;">SARIMAX</h4>
            <div style="color:var(--np-muted); font-size:0.9rem; line-height:1.7;">
                Captures seasonal cycles and<br>linear macroeconomic relationships
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="np-card" style="text-align:center; padding:1.8rem;">
            <div style="margin-bottom:0.8rem;">
                <i class="icofont-tree np-icon-primary" style="font-size:2.2rem;"></i>
            </div>
            <h4 style="color:var(--np-primary); margin-bottom:0.8rem;">Random Forest</h4>
            <div style="color:var(--np-muted); font-size:0.9rem; line-height:1.7;">
                Captures non-linear patterns<br>and structural break behaviour
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="np-card" style="text-align:center; padding:1.8rem;">
            <div style="margin-bottom:0.8rem;">
                <i class="icofont-network np-icon-primary" style="font-size:2.2rem;"></i>
            </div>
            <h4 style="color:var(--np-primary); margin-bottom:0.8rem;">LSTM Network</h4>
            <div style="color:var(--np-muted); font-size:0.9rem; line-height:1.7;">
                Captures sequential dependencies<br>and long-term temporal memory
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Meta-Learner
    st.markdown(f"""
    <div style="text-align:center; margin:2rem 0;">
        <div style="display:inline-block; background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); 
                    padding:1.8rem 3rem; border-radius:16px; color:white;">
            <i class="icofont-flash icofont-xl" style="color:white; font-size:1.6rem; margin-right:0.5rem;"></i>
            <strong style="font-size:1.4rem;">XGBoost Meta-Learner</strong><br>
            <span style="opacity:0.95; font-size:1rem;">
                Learns the optimal combination of all three base model predictions
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Call to Action
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        if st.button("OPEN FORECAST TERMINAL", use_container_width=True, type="primary"):
            st.switch_page(st.session_state.forecast_page)

    st.markdown("<br>", unsafe_allow_html=True)

    # Trust Indicators
    st.markdown("---")

    trust_col1, trust_col2, trust_col3, trust_col4 = st.columns(4)

    indicators = [
        ("icofont-book", "25+ Years", "Historical CPI Data"),
        ("icofont-laboratory", "65 Features", "Engineered Variables"),
        ("icofont-layers", "4 Models", "Stacked Ensemble"),
        ("icofont-pie-chart", "3 Categories", "Consumer Price Forecasts"),
    ]

    for col, (icon_class, value, label) in zip(
        [trust_col1, trust_col2, trust_col3, trust_col4], indicators
    ):
        with col:
            st.markdown(f"""
            <div style="text-align:center; padding:1rem 0;">
                <i class="{icon_class} np-icon-primary" style="font-size:2rem;"></i>
                <div style="font-weight:700; font-size:1.3rem; margin:0.5rem 0; color:var(--np-primary);">
                    {value}
                </div>
                <div style="color:var(--np-muted); font-size:0.85rem;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()