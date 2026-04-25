# pages/home.py
import streamlit as st
from app.config import THEME

def show_home():
    # Hero Section
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {THEME['primary']} 0%, #3B82F6 100%); padding: 5rem 2rem; border-radius: 24px; color: white; margin-bottom: 3rem; text-align: center; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);">
            <h1 style="font-size: 4.5rem; font-weight: 900; margin-bottom: 1rem; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">NairaPulse AI</h1>
            <p style="font-size: 1.6rem; opacity: 0.95; max-width: 850px; margin: 0 auto; line-height: 1.4; font-weight: 300;">
                Precision Intelligence for Nigeria's Consumer Economy. 
                Forecasting the pulse of essential commodity prices through advanced AI.
            </p>
            <div style="margin-top: 3rem; display: flex; justify-content: center; gap: 1.5rem;">
                <div style="background: white; color: {THEME['primary']}; padding: 0.8rem 2rem; border-radius: 50px; font-weight: 700; font-size: 1rem;">STACKED ENSEMBLE v2.5</div>
                <div style="background: {THEME['secondary']}; color: {THEME['text']}; padding: 0.8rem 2rem; border-radius: 50px; font-weight: 700; font-size: 1rem;">ABUAD COMPUTING</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Why NairaPulse AI
    col1, col2 = st.columns([2.8, 1.2])
    with col1:
        st.markdown(f"### <span style='color: {THEME['primary']}'>💡 Why NairaPulse AI Matters</span>", unsafe_allow_html=True)
        st.markdown("""
        Nigeria’s consumer prices are highly sensitive to macroeconomic forces such as exchange rate volatility and global oil shocks. 
        **NairaPulse AI** bridges the gap between raw data and actionable foresight. 
        By synthesizing econometric rigor with deep learning memory, we help you anticipate market shifts with institutional confidence.
        """)
    with col2:
        st.info("""
        **Benchmark Rates**
        - Inflation: **15.88%**
        - FX Rate: **₦1,556.89 / USD**
        - Oil Price: **$82.50 / barrel**
        """)

    st.write("---")

    # ==================== TARGET CATEGORIES REDESIGN ====================
    st.markdown(f"### <span style='color: {THEME['primary']}'>🎯 Core Sector Pulses</span>", unsafe_allow_html=True)
    st.markdown("We focus on the three pillars of the Nigerian household basket. Select a sector to understand why it's critical.")

    cat_data = {
        "Food": {
            "emoji": "🥘", 
            "color": "#10B981", 
            "why": "Food represents over 50% of the average Nigerian household's expenditure. It is highly sensitive to both climate shocks and imported inflation from exchange rate shifts.",
            "desc": "Grains, imported food, and farm produce."
        },
        "Transport": {
            "emoji": "🚗", 
            "color": "#3B82F6", 
            "why": "Transport is the circulatory system of the economy. Fuel price deregulation and oil price shifts propagate through transport costs into the prices of all other goods.",
            "desc": "Inter-city and intra-city logistics costs."
        },
        "Clothing": {
            "emoji": "👕", 
            "color": "#F59E0B", 
            "why": "A sector dominated by imports. Clothing price dynamics serve as a primary indicator of exchange rate pass-through and consumer discretionary spending health.",
            "desc": "Apparel and essential consumer wear."
        }
    }

    cols = st.columns(3)
    for i, (name, data) in enumerate(cat_data.items()):
        with cols[i]:
            st.markdown(f"""
            <div style='background: white; border-top: 8px solid {data["color"]}; border-radius: 20px; padding: 2rem 1.5rem; text-align: center; height: 320px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1); margin-bottom: 1rem;'>
                <div style='font-size: 3.5rem; margin-bottom: 1rem;'>{data["emoji"]}</div>
                <h3 style='margin: 0 0 0.5rem 0; color: {THEME["text"]}; font-weight: 800; font-size: 1.5rem;'>{name}</h3>
                <p style='margin: 0; font-size: 0.95rem; color: #475569; line-height: 1.5;'><b>Why:</b> {data["why"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Read More button for each category
            if st.button(f"Read more about {name}", key=f"read_more_{name}", use_container_width=True):
                st.session_state.page = "ℹ️ About"
                st.rerun()

    st.write("---")

    # Call to Action
    st.markdown(f"""
    <div style='text-align: center; padding: 4rem 2rem; background: {THEME['primary']}; color: white; border-radius: 24px; margin: 2.5rem 0; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);'>
        <h2 style='color: white; margin-bottom: 1.5rem; font-weight: 800;'>Execute Strategic Scenarios</h2>
        <p style='font-size: 1.3rem; margin-bottom: 2.5rem; opacity: 0.9; max-width: 700px; margin-left: auto; margin-right: auto;'>
            Harness the power of NairaPulse AI to simulate how macroeconomic shocks ripple through the economy.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 GO TO FORECAST", use_container_width=True):
        st.session_state.page = "📈 Forecast"
        st.rerun()

    st.caption("Final Year Project • Chimbueze David • Department of Computing • ABUAD")

if __name__ == "__main__":
    show_home()