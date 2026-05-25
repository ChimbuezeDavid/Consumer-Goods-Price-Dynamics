# app/pages/about.py
"""
NairaPulse AI - Methodology Page
Publication-quality content with IcoFont icons. No emojis.
"""

import streamlit as st
from app.ui_components import render_hero, render_section_header

def show_about():
    """Render methodology page with professional layout and copy."""
    render_hero(
        title="Methodology",
        subtitle="A rigorous account of the data, feature engineering, model architecture, and validation approach behind NairaPulse AI's forecasting system."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Project Objective
    render_section_header(
        '<i class="icofont-target np-icon-primary"></i>',
        "Research Objective"
    )

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("""
        Nigeria's consumer price index has been one of the most volatile among major African economies 
        over the past decade, driven by persistent currency pressure, energy subsidy reforms, supply-chain 
        disruptions, and structural food production constraints.

        **NairaPulse AI** addresses a critical gap in accessible, data-driven inflation intelligence by 
        forecasting **month-over-month** price changes across three categories that together represent 
        the majority of household expenditure:

        - **Food** -- approximately 50% of household budgets; driven by seasonal harvests, 
          exchange rate pass-through, and fuel costs for agricultural logistics.
        - **Transport** -- approximately 12% of household budgets; a direct function of 
          global crude oil benchmarks and domestic fuel pricing policy.
        - **Clothing & Footwear** -- approximately 6% of household budgets; highly 
          import-dependent, tracking naira depreciation with a short lag.

        The system is designed to support **researchers, policymakers, procurement teams, and 
        development practitioners** seeking transparent, reproducible, and interpretable price forecasts 
        beyond what simple autoregressive or seasonal decomposition models provide.
        """)

    with col2:
        st.markdown("""
        <div class="np-card" style="text-align:center;">
            <i class="icofont-data np-icon-primary" style="font-size:2.5rem;"></i>
            <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary); margin:1rem 0;">
                25+ Years
            </div>
            <div style="color:var(--np-muted);">Monthly CPI Data<br>(January 2000 &ndash; February 2026)</div>
        </div>
        <br>
        <div class="np-card" style="text-align:center;">
            <i class="icofont-world np-icon-primary" style="font-size:2.5rem;"></i>
            <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary); margin:1rem 0;">
                313
            </div>
            <div style="color:var(--np-muted);">Monthly Observations<br>in Training Corpus</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Technical Architecture
    render_section_header(
        '<i class="icofont-architecture np-icon-primary"></i>',
        "Model Architecture"
    )

    st.markdown("""
    The system employs a **stacked generalization** framework, a meta-learning approach in which 
    multiple heterogeneous base learners are trained independently, and a higher-order meta-learner 
    is trained to optimally combine their out-of-sample predictions. This architecture exploits the 
    complementary strengths of each model family while avoiding over-reliance on any single 
    modelling assumption.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Base Learners
    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        st.markdown("""
        <div class="np-card" style="height:100%; text-align:center;">
            <div style="margin-bottom:1rem;">
                <i class="icofont-chart-line np-icon-primary" style="font-size:2.5rem;"></i>
            </div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">SARIMAX</h3>
            <div style="color:var(--np-muted); line-height:1.9; text-align:left;">
                <strong>Captures:</strong><br>
                &bull; Annual seasonal cycles<br>
                &bull; Linear trend components<br>
                &bull; Macroeconomic exogenous inputs<br>
                &bull; Autocorrelation structure
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="np-card" style="height:100%; text-align:center;">
            <div style="margin-bottom:1rem;">
                <i class="icofont-tree np-icon-primary" style="font-size:2.5rem;"></i>
            </div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Random Forest</h3>
            <div style="color:var(--np-muted); line-height:1.9; text-align:left;">
                <strong>Captures:</strong><br>
                &bull; Non-linear feature interactions<br>
                &bull; Regime changes &amp; structural breaks<br>
                &bull; High-dimensional feature spaces<br>
                &bull; Robust to outliers
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="np-card" style="height:100%; text-align:center;">
            <div style="margin-bottom:1rem;">
                <i class="icofont-network np-icon-primary" style="font-size:2.5rem;"></i>
            </div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">LSTM Network</h3>
            <div style="color:var(--np-muted); line-height:1.9; text-align:left;">
                <strong>Captures:</strong><br>
                &bull; Long-range temporal dependencies<br>
                &bull; Sequential memory effects<br>
                &bull; Gradient-based pattern learning<br>
                &bull; Dynamic volatility periods
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Meta-Learner
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); 
                padding:2.5rem; border-radius:16px; color:white; text-align:center;">
        <i class="icofont-flash" style="font-size:2rem; color:white; margin-bottom:0.5rem; display:block;"></i>
        <h3 style="color:white; margin:0 0 1rem 0;">XGBoost Meta-Learner</h3>
        <p style="opacity:0.95; margin:0; font-size:1.05rem; max-width:600px; margin:0 auto;">
            A gradient-boosted meta-learner trained on the out-of-fold predictions of all three base 
            models, learning their optimal combination weights. This final layer consistently 
            outperforms any single base model in held-out evaluation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Feature Engineering
    render_section_header(
        '<i class="icofont-laboratory np-icon-primary"></i>',
        "Feature Engineering"
    )

    st.markdown("""
    A systematic feature engineering pipeline produces **65 input variables** across 9 conceptual 
    groups from four raw data sources: NBS Consumer Price Index series, CBN official exchange 
    rates, EIA Brent crude oil prices, and a manually curated structural break catalogue.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    feat_col1, feat_col2 = st.columns(2, gap="large")

    with feat_col1:
        st.markdown("""
        **Input Feature Groups:**

        - **Macroeconomic levels** -- exchange rate (USD/NGN), Brent crude (USD/barrel), headline CPI
        - **Lagged values** -- 1, 2, and 3-month lags of all macro variables and CPI sub-indices
        - **Rolling statistics** -- 3-month and 6-month rolling means, standard deviations, and min/max windows
        - **Month-over-month lags** -- lagged MoM changes for the three target categories
        """)

    with feat_col2:
        st.markdown("""
        &nbsp;

        - **Derived interactions** -- oil price multiplied by exchange rate (import cost proxy)
        - **Cyclical encoding** -- sine/cosine encoding of calendar month to capture seasonality continuously
        - **Structural break dummies** -- binary indicators for COVID-19 shock (2020), fuel subsidy removal (2023), FX unification (2023)
        - **Cross-category spillover** -- lagged values of sibling category MoM changes as predictors
        - **Trend features** -- linear trend variable and year-over-year growth rates
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Technology Stack
    render_section_header(
        '<i class="icofont-code np-icon-primary"></i>',
        "Technology Stack"
    )

    tech_cols = st.columns(4, gap="medium")

    techs = [
        ("icofont-brand-python", "Python 3.10"),
        ("icofont-layers", "TensorFlow 2"),
        ("icofont-laboratory", "Scikit-learn"),
        ("icofont-chart-bar-graph", "Statsmodels"),
        ("icofont-flash", "XGBoost"),
        ("icofont-monitor", "Streamlit"),
        ("icofont-chart-line", "Plotly"),
        ("icofont-table", "Pandas / NumPy"),
    ]

    for i, (icon_class, tech_name) in enumerate(techs):
        with tech_cols[i % 4]:
            st.markdown(f"""
            <div class="np-card" style="text-align:center; padding:1.5rem;">
                <i class="{icon_class} np-icon-primary" style="font-size:2.2rem; margin-bottom:0.5rem; display:block;"></i>
                <div style="font-weight:700; color:var(--np-primary); font-size:0.95rem;">{tech_name}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Developer Info
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); 
                color:white; padding:3rem; border-radius:16px; text-align:center;">
        <div style="color:rgba(255,255,255,0.75); font-weight:700; letter-spacing:1px; 
                    font-size:0.8rem; margin-bottom:1rem; text-transform:uppercase;">
            Research &amp; Development
        </div>
        <div style="font-size:2.4rem; font-weight:800; margin-bottom:0.8rem;">
            Chimbueze David
        </div>
        <div style="opacity:0.95; font-size:1.05rem; line-height:1.8;">
            Department of Computing<br>
            Afe Babalola University (ABUAD), Ado-Ekiti, Nigeria<br>
            <span style="font-size:0.9rem; opacity:0.8;">Undergraduate Research Project, 2025/2026 Academic Year</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_about()