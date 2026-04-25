# pages/about.py
import streamlit as st
from app.config import THEME

def show_about():
    # Elite Header
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {THEME['primary']} 0%, #1e3a8a 100%); padding: 4rem 2rem; border-radius: 24px; color: white; margin-bottom: 3rem; text-align: center;">
            <h1 style="color: white; font-weight: 900; font-size: 3.5rem; margin-bottom: 1rem;">The Architect & The Algorithm</h1>
            <p style="font-size: 1.4rem; opacity: 0.9;">Unveiling the Engineering Excellence of NairaPulse AI</p>
        </div>
    """, unsafe_allow_html=True)

    # Bragadocious Developer Section
    st.markdown(f"### <span style='color: {THEME['primary']}'>🚀 Visionary Engineering: Chimbueze David</span>", unsafe_allow_html=True)
    st.markdown(f"""
    NairaPulse AI is the culmination of rigorous research and technical mastery by **Chimbueze David**. 
    In an era of simplistic forecasting, Chimbueze has pioneered a **Heterogeneous Stacked Ensemble** that outperforms traditional benchmarks. 
    By orchestrating SARIMAX, LSTMs, and Random Forests into a single unified predictive pulse, he has delivered a tool that captures the 
    very essence of the Nigerian economic heartbeat.
    
    This is not just code; it is a strategic asset for economic foresight, developed within the elite halls of **ABUAD Computing**.
    """)

    st.write("---")

    # Monte Carlo & Stochastic Necessity
    st.markdown(f"### <span style='color: {THEME['primary']}'>🎲 The Necessity of Randomness: Monte Carlo Philosophy</span>", unsafe_allow_html=True)
    st.markdown("""
    Why does NairaPulse AI include randomness? Because the real world is not deterministic. 
    Traditional models fail precisely where they claim certainty. 
    
    By integrating **Stochastic Noise injection**, inspired by **Monte Carlo simulation principles**, NairaPulse AI acknowledges 
    the "unknown unknowns"—the sudden policy shifts, the localized market panics, and the global ripples that macroeconomic variables alone 
    cannot predict. We don't just provide a target; we provide a probabilistic pulse that reflects the true risk-profile of the Nigerian market.
    """)

    st.write("---")

    # Concise Technical Summary
    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        st.markdown(f"#### <span style='color: {THEME['primary']}'>Methodology Reference</span>", unsafe_allow_html=True)
        st.markdown("""
        For a deep-dive into the mathematical proofs and data validation, refer to:
        - **📄 Chimbueze's project.docx** (Official Research Documentation)
        - **Model Logic:** Level-0 Base Learners + Level-1 XGBoost Meta-Learner.
        """)
    
    with col_b:
        st.markdown(f"#### <span style='color: {THEME['primary']}'>Technical Stack</span>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 15px; border-left: 5px solid {THEME['secondary']}; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">
            <b>Framework:</b> Streamlit<br>
            <b>AI:</b> TensorFlow, Sklearn, XGBoost<br>
            <b>Stats:</b> Statsmodels (SARIMAX)
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_about()