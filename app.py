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

# Hide Streamlit watermarks
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    #GithubIcon {visibility: hidden;}

    .viewerBadge_container__1QSob,
    .viewerBadge_container__3yXjG,
    [class^="viewerBadge_container"],
    [class*="viewerBadge"],
    #viewerBadge_container,
    .stDeployButton,
    [data-testid="stAppDeployButton"],
    iframe[src*="badge"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

    /* Hide toolbar chrome & decoration — NOT the header wrapper itself */
    [data-testid="stToolbarActions"] {
        display: none !important;
    }
    [data-testid="stDecoration"] {
        display: none !important;
    }
    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    /* Keep header transparent so hamburger button remains visible & clickable */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* But re-enable pointer events on the hamburger button itself */
    [data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        pointer-events: all !important;
        z-index: 9999 !important;
    }

    [data-testid="collapsedControl"] svg,
    [data-testid="collapsedControl"] span {
        color: var(--np-primary) !important;
        fill: var(--np-primary) !important;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# PWA meta tags (st.markdown handles HTML meta/link tags fine, just not <script>)
st.markdown("""
<link rel="manifest" href="/app/static/manifest.json">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="NairaPulse AI">
<meta name="theme-color" content="#0F172A">
<link rel="apple-touch-icon" href="/app/static/icon-192.png">
""", unsafe_allow_html=True)

# JavaScript must be injected via st.components.v1.html — st.markdown does NOT execute scripts
import streamlit.components.v1 as components
components.html("""
<script>
// 1. Automatically redirect to the embedded/chromeless version if accessed directly on the standalone URL
try {
    if (parent && parent.location && !parent.location.search.includes('embed=true')) {
        const url = new URL(parent.location.href);
        url.searchParams.set('embed', 'true');
        parent.location.replace(url.href);
    }
} catch (e) {
    console.warn("Could not check/redirect parent location:", e);
}

// 2. Register service worker for PWA on the parent context (fallback to local iframe)
try {
    if (parent && 'serviceWorker' in parent.navigator) {
        parent.navigator.serviceWorker.register('/app/static/sw.js')
            .then(reg => console.log('ServiceWorker registered on parent:', reg.scope))
            .catch(err => console.error('ServiceWorker registration failed on parent:', err));
    } else if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/app/static/sw.js');
    }
} catch (e) {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/app/static/sw.js');
    }
}

// 3. Remove the Streamlit "Manage app" button / badge dynamically
function removeManageApp() {
    const selectors = [
        '[data-testid="stAppDeployButton"]',
        '.stDeployButton',
        'a[href*="share.streamlit.io"]',
        '[class*="deployButton"]',
        '[class*="manageApp"]',
        '[class*="manage-app"]',
    ];
    // Clear in parent window
    try {
        if (parent && parent.document) {
            selectors.forEach(sel => {
                parent.document.querySelectorAll(sel).forEach(el => el.remove());
            });
            parent.document.querySelectorAll('button, a, div, span').forEach(el => {
                if (el.textContent.trim() === 'Manage app') {
                    (el.closest('[class]') || el).remove();
                }
            });
        }
    } catch (e) {}
    // Clear in local iframe (fallback)
    selectors.forEach(sel => {
        document.querySelectorAll(sel).forEach(el => el.remove());
    });
    document.querySelectorAll('button, a, div, span').forEach(el => {
        if (el.textContent.trim() === 'Manage app') {
            (el.closest('[class]') || el).remove();
        }
    });
}

try {
    removeManageApp();
    if (parent && parent.document && parent.document.body) {
        const observer = new MutationObserver(removeManageApp);
        observer.observe(parent.document.body, { childList: true, subtree: true });
    } else {
        const observer = new MutationObserver(removeManageApp);
        observer.observe(document.body, { childList: true, subtree: true });
    }
} catch (e) {
    const observer = new MutationObserver(removeManageApp);
    observer.observe(document.body, { childList: true, subtree: true });
}
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