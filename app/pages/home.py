# pages/home.py
"""
NairaPulse AI - Home Page
Clean light theme with uniform cards and stacked ensemble section.
"""

import streamlit as st
from app.ui_components import render_hero, render_section_header, render_card, render_tech_badge

def show_home():
    """Main landing page with refined content and visual hierarchy."""
    render_hero(
        title="NairaPulse AI",
        subtitle="Understanding Nigeria’s price movements — one month at a time. Thoughtfully built to bring clarity to everyday economic realities."
    )

    col_a, col_b = st.columns([2, 1], gap="large")

    with col_a:
        st.markdown("""
        ### The Human Story Behind the Numbers

        In Nigeria, price changes are deeply personal. They determine what families can afford for food, transport to work, 
        and basic clothing. **Month-over-month movements** reveal the real shocks and moments of relief that annual figures often hide.
        """)
        
        st.info("""
        NairaPulse AI combines 25+ years of macroeconomic data with a stacked ensemble model and domain-tuned heuristics 
        to deliver realistic, transparent forecasts for the categories that matter most.
        """)

    with col_b:
        st.markdown(f"""
        <div class="np-card" style="height:100%;">
            <h4 style="margin-top:0;">Current Economic Snapshot</h4>
            <div style="font-size:2.2rem; font-weight:800; color:var(--np-success);">15.38%</div>
            <div style="color:var(--np-muted);">Latest Headline Inflation</div>
            <hr style="margin:1.5rem 0; border:0; border-top:1px solid var(--np-border);">
            <div style="display:flex; justify-content:space-between; margin:0.8rem 0;">
                <span style="font-weight:600;">₦1,351.35</span>
                <span style="color:var(--np-muted);">Official FX Rate</span>
            </div>
            <div style="display:flex; justify-content:space-between;">
                <span style="font-weight:600;">$105.33</span>
                <span style="color:var(--np-muted);">Brent Crude Oil</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)
    render_section_header("📍", "Key Price Categories")

    # Uniform cards
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="uniform-card">', unsafe_allow_html=True)
        render_card("Food Category", 
                    "The cornerstone of household inflation. Highly responsive to exchange rate movements and domestic agricultural supply conditions.", 
                    icon="🍽️")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="uniform-card">', unsafe_allow_html=True)
        render_card("Transport Category", 
                    "Major channel through which global energy prices affect the domestic economy. Serves as a leading indicator of broader cost pressures.", 
                    icon="🚗")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="uniform-card">', unsafe_allow_html=True)
        render_card("Clothing & Footwear Category", 
                    "Strongly import-dependent category. Provides one of the clearest early signals of exchange rate pass-through effects.", 
                    icon="👕")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    render_section_header("🧠", "How Our Engine Works")

    # Base models
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1: render_tech_badge("SARIMAX", "Seasonal & Econometric")
    with col2: render_tech_badge("Random Forest", "Non-linear Interactions")
    with col3: render_tech_badge("LSTM", "Sequential Patterns")

    # Stacked Ensemble (Centred)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align:center; margin:2rem 0;">
        <div style="display:inline-block; background:var(--np-surface); padding:1rem 2.5rem; 
                    border-radius:12px; border:2px solid var(--np-primary);">
            <strong style="color:var(--np-primary);">STACKED ENSEMBLE META-LEARNER</strong><br>
            <span style="color:var(--np-muted);">Combines predictions from all base models with economic heuristics</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        if st.button("🚀 OPEN FORECAST TERMINAL", use_container_width=True, type="primary"):
            st.switch_page(st.session_state.forecast_page)

if __name__ == "__main__":
    show_home()