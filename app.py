# app.py
import streamlit as st
import sys
from pathlib import Path

# No need to manually append to sys.path since we use package-style imports

from app.config import PAGE_CONFIG, CUSTOM_CSS, BRAND_NAME

st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

from app.pages.home import show_home
from app.pages.forecast import show_forecast
from app.pages.about import show_about
from app.pages.contact import show_contact

# Initialize Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Define Pages for st.navigation
pages = [
    st.Page(show_home, title="Home", icon="🏠", url_path="home", default=(st.session_state.page == "home")),
    st.Page(show_forecast, title="Forecast Engine", icon="📈", url_path="forecast"),
    st.Page(show_about, title="About Methodology", icon="ℹ️", url_path="about"),
    st.Page(show_contact, title="Contact Developer", icon="📞", url_path="contact"),
]

# Run Navigation
pg = st.navigation(pages)

# Custom Sidebar Branding (Standard for premium apps)
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem;">
            <h1 style="color: white; margin: 0; font-size: 1.8rem;"> {BRAND_NAME}</h1>
            <p style="color: #94a3b8; font-size: 0.8rem; margin-top: 0.5rem; letter-spacing: 1px;">FORECASTING INTELLIGENCE</p>
        </div>
    """, unsafe_allow_html=True)

# Run the selected page
pg.run()

# Centralized Footer (Ensuring it runs on all pages)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; color: #64748b; font-size: 0.9rem; border-top: 2px solid gold; padding-top: 2rem; margin-top: 2rem;">
        © 2026 NairaPulse AI • Built with Passion for Nigeria's Economic Development • {BRAND_NAME}
    </div>
""", unsafe_allow_html=True)