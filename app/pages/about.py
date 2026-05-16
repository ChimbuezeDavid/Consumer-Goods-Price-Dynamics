# app/pages/about.py
"""
NairaPulse AI - Clean Methodology Page
Removed performance table, better spacing, less crowded.
"""

import streamlit as st
from app.ui_components import render_hero, render_section_header, render_card

def show_about():
    """Render methodology page with clean layout."""
    render_hero(
        title="Methodology",
        subtitle="How NairaPulse AI forecasts Nigerian consumer goods price dynamics."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Project Objective
    render_section_header("🎯", "Project Objective")
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        NairaPulse AI forecasts **month-over-month** price changes in three critical categories:
        
        - **Food** (~50% of household budgets)
        - **Transport** (~12% of household budgets)
        - **Clothing & Footwear** (~6% of household budgets)
        
        These categories account for over 70% of Nigerian household expenditure and exhibit 
        distinct responses to economic shocks.
        """)
    
    with col2:
        st.markdown("""
        <div class="np-card" style="text-align:center;">
            <div style="font-size:2.5rem;">📊</div>
            <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary); margin:1rem 0;">
                25+ Years
            </div>
            <div style="color:var(--np-muted);">Historical Data<br>(2000-2026)</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Technical Architecture
    render_section_header("🔬", "Technical Architecture")
    
    st.markdown("""
    A **stacked ensemble** combines three specialized models, each capturing different aspects 
    of price dynamics. A meta-learner then optimally combines their predictions.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Base Learners - Cleaner cards
    c1, c2, c3 = st.columns(3, gap="large")
    
    with c1:
        st.markdown("""
        <div class="np-card" style="height:100%; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:1rem;">📈</div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">SARIMAX</h3>
            <div style="color:var(--np-muted); line-height:1.8;">
                <strong>Captures:</strong><br>
                • Seasonal patterns<br>
                • Linear trends<br>
                • Macro relationships
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="np-card" style="height:100%; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:1rem;">🌳</div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Random Forest</h3>
            <div style="color:var(--np-muted); line-height:1.8;">
                <strong>Captures:</strong><br>
                • Non-linear patterns<br>
                • Structural breaks<br>
                • Feature interactions
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with c3:
        st.markdown("""
        <div class="np-card" style="height:100%; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:1rem;">🧠</div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">LSTM</h3>
            <div style="color:var(--np-muted); line-height:1.8;">
                <strong>Captures:</strong><br>
                • Temporal dependencies<br>
                • Sequential patterns<br>
                • Long-term memory
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Meta-Learner
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); 
                padding:2.5rem; border-radius:16px; color:white; text-align:center;">
        <h3 style="color:white; margin:0 0 1rem 0;">⚡ XGBoost Meta-Learner</h3>
        <p style="opacity:0.95; margin:0; font-size:1.05rem;">
        Combines the three base predictions using learned optimal weights
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Feature Engineering
    render_section_header("⚙️", "Feature Engineering")
    
    feat_col1, feat_col2 = st.columns(2, gap="large")
    
    with feat_col1:
        st.markdown("""
        **65 Engineered Features across 9 groups:**
        
        - Macro variables (exchange rate, oil price)
        - Lagged values (1-3 months)
        - Rolling statistics (3-month, 6-month windows)
        - Target month-over-month lags
        """)
    
    with feat_col2:
        st.markdown("""
        - Derived features (oil × FX interaction)
        - Cyclical encoding (month sin/cos)
        - Structural break dummies (COVID-19, devaluations)
        - Cross-category spillover effects
        """)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Technology Stack
    render_section_header("🛠️", "Technology Stack")

    tech_cols = st.columns(4, gap="medium")
    
    techs = [
        ("Python", "🐍"),
        ("TensorFlow", "🧠"),
        ("Scikit-learn", "🔬"),
        ("Statsmodels", "📊"),
        ("XGBoost", "⚡"),
        ("Streamlit", "🌐"),
        ("Plotly", "📈"),
        ("Pandas", "🔢")
    ]
    
    for i, (tech, icon) in enumerate(techs):
        with tech_cols[i % 4]:
            st.markdown(f"""
            <div class="np-card" style="text-align:center; padding:1.5rem;">
                <div style="font-size:2.5rem; margin-bottom:0.5rem;">{icon}</div>
                <div style="font-weight:700; color:var(--np-primary);">{tech}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Developer Info
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); 
                color:white; padding:3rem; border-radius:16px; text-align:center;">
        <div style="color:rgba(255,255,255,0.9); font-weight:700; letter-spacing:1px; 
                    font-size:0.9rem; margin-bottom:1rem;">
            DEVELOPED BY
        </div>
        <div style="font-size:2.6rem; font-weight:800; margin-bottom:1rem;">
            Chimbueze David
        </div>
        <div style="opacity:0.95; font-size:1.1rem;">
            Department of Computing • Afe Babalola University
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_about()