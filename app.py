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

# PWA meta tags (these are HTML-only, no script needed here)
st.markdown("""
<link rel="manifest" href="/app/static/manifest.json">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="NairaPulse AI">
<meta name="theme-color" content="#0F172A">
<link rel="apple-touch-icon" href="/app/static/icon-192.png">
""", unsafe_allow_html=True)

# JavaScript MUST be injected via components.html — st.markdown strips <script> tags
import streamlit.components.v1 as components
components.html("""
<script>
(function() {
    function removeManageApp() {
        const doc = window.parent.document;

        // Target by data-testid
        const selectors = [
            '[data-testid="stAppDeployButton"]',
            '[data-testid="stDeployButton"]',
            '.stDeployButton',
            '[class*="deployButton"]',
            '[class*="manageApp"]',
            '[class*="manage-app"]',
            '[class*="ManageApp"]',
        ];
        selectors.forEach(sel => {
            doc.querySelectorAll(sel).forEach(el => {
                el.style.display = 'none';
                el.remove();
            });
        });

        // Fallback: remove any element whose visible text is exactly "Manage app"
        doc.querySelectorAll('button, a, span, div').forEach(el => {
            if (el.childElementCount === 0 && el.textContent.trim() === 'Manage app') {
                let target = el;
                // Walk up to remove the whole container widget
                for (let i = 0; i < 5; i++) {
                    if (target.parentElement) target = target.parentElement;
                }
                target.style.display = 'none';
            }
        });
    }

    // Register PWA service worker from parent context
    if ('serviceWorker' in window.parent.navigator) {
        window.parent.navigator.serviceWorker.register('/app/static/sw.js');
    }

    // Run immediately and watch for dynamic injections
    removeManageApp();
    const observer = new MutationObserver(removeManageApp);
    observer.observe(window.parent.document.body, { childList: true, subtree: true });
})();
</script>
""", height=0)

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