import streamlit as st
import os
from app.config import CATEGORIES

import streamlit as st

st.set_page_config(
    page_title="Nigeria CPI Forecaster",
    page_icon="🇳🇬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation + Improved Style
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h2 style='color: #1E3A8A; margin: 0;'>🇳🇬 CPI Forecaster</h2>
        <p style='font-size: 0.9rem; color: #64748B; margin: 0.5rem 0 0 0;'>Stacked Ensemble Model</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["🏠 Home", "📈 Forecast", "ℹ️ About", "📞 Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Current Rates in Sidebar
    st.markdown("**Current Rates (April 2026)**")
    st.markdown("""
    - Food Inflation: **12.12%**  
    - Core Inflation: **15.88%**  
    - Exchange: **₦1,356.89/USD**  
    - Oil: **$95.20/barrel**
    """)

# Page Routing
if page == "🏠 Home":
    from app.pages.home import show_home
    show_home()
elif page == "📈 Forecast":
    from app.pages.forecast import show_forecast
    show_forecast()
elif page == "ℹ️ About":
    from app.pages.about import show_about
    show_about()
elif page == "📞 Contact":
    from app.pages.contact import show_contact
    show_contact()

# Consistent Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1.5rem; color: #64748B; font-size: 0.9rem;'>
    Final Year Project • Department of Computing • Afe Babalola University, Ado-Ekiti (ABUAD)<br>
    Built with SARIMAX • Random Forest • LSTM • XGBoost
</div>
""", unsafe_allow_html=True)