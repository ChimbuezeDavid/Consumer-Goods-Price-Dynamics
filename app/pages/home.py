# pages/home.py
import streamlit as st
from app.config import THEME
from app.ui_components import render_hero, render_section_header, render_card, render_sidebar_info_card

def show_home():
    # Standard Hero
    render_hero(
        title="NairaPulse AI",
        subtitle="Institutional-Grade Intelligence for the Nigerian Consumer Economy. Navigating volatility through the power of Stacked Ensemble Forecasting."
    )

    # The Narrative
    col_a, col_b = st.columns([1.5, 1], gap="large")
    
    with col_a:
        render_section_header("🌪️", "The Volatility Gap")
        st.write("""
        Nigeria’s economy is defined by high-velocity shifts. Sudden currency devaluations, global oil shocks, and policy 
        recalibrations create a landscape where traditional linear models often fail.
        
        **NairaPulse AI** was born to bridge this gap. We don't just look at history; we simulate the future by 
        synthesizing econometric rigor with deep learning memory.
        """)
        
        render_section_header("💡", "Institutional Confidence")
        st.write("""
        Whether you are managing a corporate supply chain or drafting national policy, our platform provides the 
        analytical "Pulse" needed to turn macroeconomic uncertainty into strategic advantage.
        """)
    
    with col_b:
        render_sidebar_info_card("Live Macro Benchmarks", {
            "Headline Inflation": "15.38%",
            "Official FX Rate": "₦1,351.35",
            "Brent Crude Oil": "$105.33"
        })

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Sector Pulses
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 3.5rem;">
            <p style="color: {THEME['secondary']}; font-weight: 800; letter-spacing: 2px; margin-bottom: 0.5rem;">CORE ANALYTICS</p>
            <h2 style="color: {THEME['primary']}; font-weight: 900; font-size: 2.5rem; margin-top: 0;">Strategic Sector Pulses</h2>
        </div>
    """, unsafe_allow_html=True)
    
    cat_data = {
        "Food Intelligence": {
            "emoji": "🥘", 
            "color": THEME['secondary'], 
            "detail": "Predicting the pulse of Nigeria's primary survival cost driver. Essential for social stability analysis."
        },
        "Transport Dynamics": {
            "emoji": "🚗", 
            "color": "#3B82F6", 
            "detail": "Mapping the circulatory system of distribution. Analyzing the ripple effects of fuel price shifts."
        },
        "Clothing & FX": {
            "emoji": "👕", 
            "color": "#F59E0B", 
            "detail": "Tracking non-discretionary import pressure. A barometer for exchange rate pass-through."
        }
    }

    cols = st.columns(3)
    for i, (name, data) in enumerate(cat_data.items()):
        with cols[i]:
            render_card(title=name, content=data['detail'], color=data['color'], icon=data['emoji'], height="350px")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Methodology Summary
    st.markdown(f"""
        <div style="background: {THEME['primary']}; padding: 4rem 2rem; border-radius: 30px; color: white; text-align: center;">
            <h2 style="color: white; margin-bottom: 3rem;">How the Pulse is Calculated</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem;">
                <div style="max-width: 200px;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">📡</div>
                    <h4 style="color: {THEME['secondary']};">1. Data Ingestion</h4>
                    <p style="font-size: 0.9rem; opacity: 0.8;">25 years of macro history fused with real-time oil and FX feeds.</p>
                </div>
                <div style="max-width: 200px;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
                    <h4 style="color: {THEME['secondary']};">2. Stacked Processing</h4>
                    <p style="font-size: 0.9rem; opacity: 0.8;">SARIMAX, RF, and LSTM base layers synthesized by XGBoost.</p>
                </div>
                <div style="max-width: 200px;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">📈</div>
                    <h4 style="color: {THEME['secondary']};">3. Pulse Output</h4>
                    <p style="font-size: 0.9rem; opacity: 0.8;">Actionable MoM forecasts with stochastic shock simulation.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Sophisticated Institutional Terminal CTA
    st.markdown(f"""
        <div style="background: linear-gradient(145deg, {THEME['sidebar']} 0%, #020617 100%); 
                    padding: 6rem 3rem; border-radius: 40px; 
                    text-align: center; border: 2px solid {THEME['secondary']}; 
                    box-shadow: 0 0 40px {THEME['secondary']}20, 0 30px 60px -12px rgba(0, 0, 0, 0.8); 
                    margin-top: 6rem; position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, transparent, {THEME['secondary']}, transparent);"></div>
            <p style="color: {THEME['secondary']}; font-weight: 800; letter-spacing: 5px; margin-bottom: 2rem;">TERMINAL STATUS: READY</p>
            <h1 style="color: white; font-weight: 900; font-size: 4rem; margin-bottom: 2rem; letter-spacing: -2px;">Unleash the Pulse Engine</h1>
            <p style="color: #E2E8F0; font-size: 1.4rem; max-width: 850px; margin: 0 auto 4rem auto; line-height: 1.7; font-weight: 300;">
                Deploy our proprietary <b>Stacked Ensemble</b> to simulate high-velocity market shocks. 
                Visualize the recursive propagation of FX and Oil dynamics across Nigeria's strategic consumer landscape.
            </p>
            <div id="launch-cta" style="display: flex; justify-content: center;">
    """, unsafe_allow_html=True)
    
    col_cta1, col_cta2, col_cta3 = st.columns([1, 1.5, 1])
    with col_cta2:
        if st.button("🚀 LAUNCH PULSE ENGINE", use_container_width=True):
            st.session_state.page = "forecast"
            st.rerun()
            
    st.markdown("</div></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()