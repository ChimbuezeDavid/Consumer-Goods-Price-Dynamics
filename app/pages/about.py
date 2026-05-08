# pages/about.py
"""
NairaPulse AI - Methodology Page
Improved with refined content flow and professionally redesigned technology stack.
"""

import streamlit as st
from app.ui_components import render_hero, render_section_header, render_card, render_tech_badge

def show_about():
    """Render the methodology page with transparent technical explanation."""
    render_hero(
        title="Methodology & Approach",
        subtitle="Clear transparency into how NairaPulse AI models Nigeria’s consumer price dynamics using ensemble intelligence and economic reasoning."
    )

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        render_section_header("🎯", "Project Objective")
        st.markdown("""
        NairaPulse AI focuses on **month-over-month** price movements in the categories that matter most to Nigerian households. 
        
        By moving beyond annual aggregates, we provide actionable foresight into the real volatility experienced by citizens and businesses.
        """)

    with col2:
        render_section_header("📊", "Focus Categories")
        with st.expander("🥘 Food Prices", expanded=True):
            st.write("Largest CPI component. Most sensitive to FX volatility and seasonal supply shocks.")
        with st.expander("🚗 Transportation", expanded=False):
            st.write("Key transmission mechanism for global oil prices into domestic costs.")
        with st.expander("👕 Clothing & Footwear", expanded=False):
            st.write("Early indicator of import-driven inflation due to exchange rate exposure.")

    st.markdown("---")

    render_section_header("🔬", "Technical Architecture")
    st.markdown("""
    A **stacked ensemble** system where SARIMAX, Random Forest, and LSTM models feed into a meta-learner. 
    Economic heuristics and controlled stochastic elements ensure forecasts remain realistic and grounded.
    """)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        render_card("SARIMAX", "Captures seasonality and direct macro relationships.", icon="📈")
    with c2:
        render_card("Random Forest", "Models complex non-linear interactions and structural breaks.", icon="🌳")
    with c3:
        render_card("LSTM", "Learns temporal dependencies in price momentum.", icon="🧠")

    st.markdown("---")

    # Redesigned Technology Stack
    render_section_header("🛠️", "Technology Stack")

    tech_data = [
        ("Python 3.12", "Core development and data pipeline"),
        ("TensorFlow / Keras", "LSTM deep learning models"),
        ("Scikit-learn", "Random Forest ensemble"),
        ("Statsmodels", "SARIMAX econometric modeling"),
        ("Streamlit", "Interactive web application"),
        ("Plotly", "High-quality interactive charts")
    ]

    cols = st.columns(3, gap="medium")
    for i, (tech, desc) in enumerate(tech_data):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="np-card" style="height:100%; text-align:center;">
                <div style="font-size:1.15rem; font-weight:700; color:var(--np-primary); margin-bottom:0.6rem;">{tech}</div>
                <div style="color:var(--np-muted); line-height:1.5;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Developer note
    st.markdown(f"""
    <div style="background:var(--np-primary); color:white; padding:2.5rem; border-radius:12px; text-align:center;">
        <div style="color:var(--np-accent); font-weight:700; letter-spacing:1px;">DEVELOPED BY</div>
        <div style="font-size:2.1rem; font-weight:800; margin:0.8rem 0;">Chimbueze David</div>
        <div style="opacity:0.9;">Final Year • Department of Computing • Afe Babalola University</div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show_about()