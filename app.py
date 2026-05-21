# app.py
"""
NairaPulse AI - Main Application Entry Point
Handles navigation, branding, dark mode toggle, and global layout.
"""

import streamlit as st

# INITIALIZE STATE
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

from app.colors import get_theme
from app.config import PAGE_CONFIG, get_custom_css, BRAND_NAME

# PAGE SETUP
st.set_page_config(**PAGE_CONFIG)

# Inject dynamic CSS based on current theme
current_theme = get_theme(st.session_state.dark_mode)
st.markdown(get_custom_css(current_theme), unsafe_allow_html=True)

# Import page functions
from app.pages.home import show_home
from app.pages.forecast import show_forecast
from app.pages.about import show_about
from app.pages.contact import show_contact

# NAVIGATION SETUP
if 'page' not in st.session_state:
    st.session_state.page = "home"

home_page = st.Page(show_home, title="Home", url_path="home", default=True)
forecast_page = st.Page(show_forecast, title="Forecast Engine", url_path="forecast")
about_page = st.Page(show_about, title="About", url_path="about")
contact_page = st.Page(show_contact, title="Contact", url_path="contact")

st.session_state.forecast_page = forecast_page
pages = [home_page, forecast_page, about_page, contact_page]

pg = st.navigation(pages)

# SIDEBAR BRANDING + DARK MODE TOGGLE
with st.sidebar:
    st.markdown(
        f"""
        <div style="padding:1.8rem 0; border-bottom:3px solid var(--np-primary); margin-bottom:2rem;">
            <div style="font-size:1.75rem; font-weight:800; color:var(--np-primary); letter-spacing:-0.02em;">
                {BRAND_NAME}
            </div>
            <div style="font-size:0.75rem; font-weight:600; color:var(--np-muted); text-transform:uppercase; letter-spacing:0.08em; margin-top:0.5rem;">
                MACROECONOMIC INTELLIGENCE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Dark Mode Toggle
    dark_mode = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    if dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_mode
        st.rerun()

# RUN SELECTED PAGE
pg.run()

# GLOBAL FOOTER
st.markdown(
    f"""
    <div style="text-align:center; padding:4rem 0 2.5rem 0; border-top:1px solid var(--np-border); 
                margin-top:5rem; color:var(--np-muted); font-size:0.9rem;">
        © 2026 {BRAND_NAME} <br>
        <span style="font-size:0.8rem; opacity:0.8;">
            Department of Computing • Afe Babalola University, Ado-Ekiti
        </span>
    </div>
    """,
    unsafe_allow_html=True
)