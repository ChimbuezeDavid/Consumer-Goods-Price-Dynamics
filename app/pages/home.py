# app/pages/home.py
"""
NairaPulse AI - Clean Home Page
Better spacing, less crowded, clearer hierarchy.
"""

import streamlit as st
from app.ui_components import render_hero, render_section_header, render_card, render_tech_badge

def show_home():
    """Landing page with clean, spacious layout."""
    render_hero(
        title="NairaPulse AI",
        subtitle="Forecasting Nigerian consumer goods price dynamics using ensemble machine learning."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Introduction
    col_a, col_b = st.columns([2, 1], gap="large")

    with col_a:
        st.markdown("""
        ### About This Tool

        NairaPulse AI forecasts **month-over-month price changes** in three key categories:
        
        - **Food** (largest household expense)
        - **Transport** (energy price channel)
        - **Clothing & Footwear** (import-dependent)
        
        These categories account for over 70% of Nigerian household spending and respond 
        differently to economic shocks like exchange rate movements and oil price changes.
        """)

    with col_b:
        st.markdown(f"""
        <div class="np-card" style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); color:white;">
            <h4 style="margin-top:0; color:white;">Latest Data</h4>
            <div style="font-size:2.2rem; font-weight:800; margin:1rem 0;">15.38%</div>
            <div style="opacity:0.9; margin-bottom:1.5rem;">Headline Inflation (MoM)</div>
            <hr style="margin:1.5rem 0; border:0; border-top:1px solid rgba(255,255,255,0.3);">
            <div style="opacity:0.9;">
                <strong>₦1,351/USD</strong> • Exchange Rate<br>
                <strong>$105/barrel</strong> • Brent Crude
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Categories - Simpler cards
    render_section_header("📍", "Forecast Categories")
    
    c1, c2, c3 = st.columns(3, gap="large")
    
    with c1:
        st.markdown("""
        <div class="np-card" style="text-align:center; height:100%;">
            <div style="font-size:3rem; margin-bottom:1rem;">🍽️</div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Food</h3>
            <div style="color:var(--np-muted); line-height:1.8;">
                Largest CPI component<br>
                Driven by FX & harvests<br>
                Typical range: -3% to +8%
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="np-card" style="text-align:center; height:100%;">
            <div style="font-size:3rem; margin-bottom:1rem;">🚗</div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Transport</h3>
            <div style="color:var(--np-muted); line-height:1.8;">
                Energy price channel<br>
                Tracks global oil<br>
                Typical range: -2% to +6%
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="np-card" style="text-align:center; height:100%;">
            <div style="font-size:3rem; margin-bottom:1rem;">👕</div>
            <h3 style="color:var(--np-primary); margin-bottom:1rem;">Clothing</h3>
            <div style="color:var(--np-muted); line-height:1.8;">
                Import-dependent<br>
                Follows exchange rate<br>
                Typical range: -1% to +4%
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Model Architecture - Simplified
    render_section_header("🧠", "Forecasting Approach")

    st.markdown("""
    Our model combines three specialized algorithms, each capturing different patterns in price data:
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div class="np-card" style="text-align:center; padding:1.8rem;">
            <div style="font-size:2rem; margin-bottom:0.8rem;">📈</div>
            <h4 style="color:var(--np-primary); margin-bottom:0.8rem;">SARIMAX</h4>
            <div style="color:var(--np-muted); font-size:0.9rem;">
                Seasonal patterns &<br>macro relationships
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="np-card" style="text-align:center; padding:1.8rem;">
            <div style="font-size:2rem; margin-bottom:0.8rem;">🌳</div>
            <h4 style="color:var(--np-primary); margin-bottom:0.8rem;">Random Forest</h4>
            <div style="color:var(--np-muted); font-size:0.9rem;">
                Non-linear patterns &<br>structural breaks
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="np-card" style="text-align:center; padding:1.8rem;">
            <div style="font-size:2rem; margin-bottom:0.8rem;">🧠</div>
            <h4 style="color:var(--np-primary); margin-bottom:0.8rem;">LSTM</h4>
            <div style="color:var(--np-muted); font-size:0.9rem;">
                Sequential patterns &<br>temporal dependencies
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Meta-Learner
    st.markdown(f"""
    <div style="text-align:center; margin:2rem 0;">
        <div style="display:inline-block; background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); 
                    padding:1.8rem 3rem; border-radius:16px; color:white;">
            <strong style="font-size:1.4rem;">⚡ XGBoost Meta-Learner</strong><br>
            <span style="opacity:0.95; font-size:1rem;">
            Combines all three predictions optimally
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Call to Action
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        if st.button("🚀 OPEN FORECAST TERMINAL", use_container_width=True, type="primary"):
            st.switch_page(st.session_state.forecast_page)

    st.markdown("<br>", unsafe_allow_html=True)

    # Trust Indicators - Simpler
    st.markdown("---")
    
    trust_col1, trust_col2, trust_col3, trust_col4 = st.columns(4)
    
    indicators = [
        ("25+ Years", "Historical Data", "📚"),
        ("65 Features", "Engineered Variables", "🎯"),
        ("4 Models", "Ensemble Stack", "⚡"),
        ("3 Categories", "Price Forecasts", "📊")
    ]
    
    for col, (value, label, icon) in zip([trust_col1, trust_col2, trust_col3, trust_col4], indicators):
        with col:
            st.markdown(f"""
            <div style="text-align:center;">
                <div style="font-size:2rem;">{icon}</div>
                <div style="font-weight:700; font-size:1.3rem; margin:0.5rem 0; color:var(--np-primary);">
                    {value}
                </div>
                <div style="color:var(--np-muted); font-size:0.85rem;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()