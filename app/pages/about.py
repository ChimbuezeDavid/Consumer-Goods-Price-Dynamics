# pages/about.py
import streamlit as st
from app.config import THEME, BRAND_NAME
from app.ui_components import render_hero, render_section_header, render_card

def show_about():
    # Standard Hero
    render_hero(
        title="NairaPulse AI",
        subtitle="Revolutionizing economic resilience through precision intelligence and stacked ensemble forecasting."
    )

    # Core Mission & "What and Why" Section
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        render_section_header("🎯", "Our Core Mission")
        st.write("""
        **NairaPulse AI** is a sophisticated forecasting platform designed to predict month-over-month 
        (MoM) percentage changes in key consumer price categories in Nigeria. 
        
        By synthesizing macroeconomic indicators — **Inflation, Exchange Rates, and Oil Prices** — we transform 
        volatile market data into institutional-grade foresight.
        """)
        
        st.info("""
        **📉 The Challenge We Solved**  
        Traditional forecasting methods often fail to capture the high-velocity volatility of the Nigerian economy. 
        NairaPulse AI bridges this gap by accounting for the non-linear "shocks" that define our market dynamics.
        """)

    with col2:
        render_section_header("📊", "What & Why We Forecast")
        
        with st.expander("🥘 Food Prices", expanded=True):
            st.markdown("""
            **What:** Monthly MoM % change in Food CPI.  
            **Why:** Food represents over **50% of household expenditure** in Nigeria. It is the primary driver of inflation and social stability.
            """)
        
        with st.expander("🚗 Transport Costs", expanded=False):
            st.markdown("""
            **What:** Monthly MoM % change in Transport CPI.  
            **Why:** Transport is the **circulatory system** of the economy. Fuel shocks propagate through transport into the price of every other physical good.
            """)
            
        with st.expander("👕 Clothing & Footwear", expanded=False):
            st.markdown("""
            **What:** Monthly MoM % change in Clothing CPI.  
            **Why:** This category is a high-sensitivity **barometer for FX pass-through**, as it relies heavily on imported materials and finished goods.
            """)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # The Science Section (Stacked Ensemble)
    st.markdown(f"""
        <div style="background: {THEME['sidebar']}; padding: 3rem; border-radius: 35px; border: 1px solid rgba(255,255,255,0.05); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); margin-bottom: 4rem;">
            <h2 style="color: white; margin-top: 0; font-weight: 800; font-size: 2.2rem; text-align: center; margin-bottom: 2rem;">🔬 The Science: Heterogeneous Stacked Ensemble</h2>
            <p style="color: #E2E8F0; margin-bottom: 3rem; font-size: 1.1rem; line-height: 1.6; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                NairaPulse AI leverages a <b>multi-layer stacked architecture</b>. Instead of relying on a single algorithm, we combine the strengths of three distinct modeling paradigms.
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
    """, unsafe_allow_html=True)
    
    sci_col1, sci_col2, sci_col3 = st.columns(3)
    with sci_col1:
        render_card("Linear (SARIMAX)", "Specialized in capturing autoregressive trends and seasonal cycles. Handles direct econometric impact.", color=THEME['secondary'], height="280px")
    with sci_col2:
        render_card("Non-Linear (RF)", "A tree-based ensemble that excels at identifying complex interactions and non-obvious thresholds.", color=THEME['secondary'], height="280px")
    with sci_col3:
        render_card("Memory (LSTM)", "A Recurrent Neural Network (RNN) that learns long-term dependencies and historical price momentum.", color=THEME['secondary'], height="280px")
        
    st.markdown(f"""
            <div style="margin-top: 3rem; padding: 2.5rem; background: linear-gradient(90deg, #92400e 0%, {THEME['secondary']} 100%); color: {THEME['text']}; border-radius: 24px; text-align: center; box-shadow: 0 10px 20px rgba(146, 64, 14, 0.3);">
                <h3 style="color: {THEME['text']}; margin: 0; font-weight: 900; font-size: 1.8rem;">Meta-Learner: XGBoost</h3>
                <p style="margin: 0.8rem 0 0 0; opacity: 0.9; font-size: 1.1rem; font-weight: 600;">
                    The ultimate arbitrator. It analyzes the output of all base models and learns the optimal way to blend their predictions.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Stochastic Section
    render_section_header("🎲", "The Role of Controlled Randomness")
    
    col_rand_1, col_rand_2 = st.columns([1.5, 1])
    
    with col_rand_1:
        st.write("""
        Economic systems in Nigeria are rarely deterministic. Factors like sudden policy shifts, global supply chain disruptions, 
        or sudden currency adjustments can cause "shocks" that no fixed model can predict perfectly.
        
        **Stochastic Simulation:**  
        By injecting controlled randomness (Gaussian noise) based on historical volatility, NairaPulse AI:
        - **Absorbs Volatility:** Better accounts for the "noise" inherent in high-velocity emerging markets.
        - **Quantifies Risk:** Produces a range of probable outcomes rather than a single, potentially overconfident value.
        - **Enhances Realism:** Mirrors the recursive and often chaotic nature of price propagation in the real world.
        """)
    
    with col_rand_2:
        st.info("""
        **"All models are wrong, but some are useful."**  
        By embracing randomness, NairaPulse AI moves from being a static calculator to a dynamic economic simulator.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Key Features Grid - Consistent Dark Style
    feat_col1, feat_col2 = st.columns(2)
    with feat_col1:
        render_card("✅ Technical Strengths", """
            <ul style="text-align: left; margin: 0; padding-left: 1.2rem;">
                <li>Trained on 25+ years of monthly macro data</li>
                <li>Advanced Lag & Rolling Statistics engineering</li>
                <li>Time-series validation (Walk-forward)</li>
                <li>Integrated stochastic Monte Carlo elements</li>
            </ul>
        """, color="#3B82F6", height="300px")
    
    with feat_col2:
        render_card("🎯 Business Value", """
            <ul style="text-align: left; margin: 0; padding-left: 1.2rem;">
                <li>High-fidelity 'What-If' scenario simulation</li>
                <li>Strategic buffer planning for procurement</li>
                <li>Policy impact analysis for stakeholders</li>
                <li>Democratized AI for economic resilience</li>
            </ul>
        """, color="#10B981", height="300px")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Developer Profile Card - Refined Gradient Design
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {THEME['primary']} 0%, #06173d 100%); 
                    padding: 5rem 2rem; border-radius: 40px; text-align: center; color: white; 
                    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); border: 1px solid rgba(255,255,255,0.05);">
            <p style="color: {THEME['secondary']}; font-weight: 800; letter-spacing: 3px; margin-bottom: 1rem; opacity: 0.9;">PROJECT DEVELOPER</p>
            <h1 style="margin: 0; color: white; font-weight: 900; font-size: 3.2rem; letter-spacing: -1px;">Chimbueze David</h1>
            <p style="font-size: 1.4rem; color: #E2E8F0; margin: 1.5rem 0; font-weight: 400;">Final Year Student, Department of Computing</p>
            <div style="background: rgba(255,255,255,0.05); display: inline-block; padding: 0.7rem 2.5rem; border-radius: 50px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem;">
                <span style="font-weight: 700; color: white;">Afe Babalola University, Ado-Ekiti (ABUAD)</span>
            </div>
            <div style="margin-top: 2rem; font-style: italic; color: #E2E8F0; font-size: 1.2rem; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.6; opacity: 0.8;">
                "NairaPulse AI represents the fusion of econometric rigor and deep learning memory, built with a passion for Nigeria’s economic future."
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_about()