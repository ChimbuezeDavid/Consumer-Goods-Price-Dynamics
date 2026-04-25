# app.py
import streamlit as st
import sys
from pathlib import Path

# Add app folder to Python path
sys.path.append(str(Path(__file__).parent / "app"))

from app.config import PAGE_CONFIG, CUSTOM_CSS

st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"

# Sidebar Navigation
with st.sidebar:
    st.title("🇳🇬 NairaPulse AI")
    st.caption("Advanced Price Dynamics Forecasting")

    # Sync radio with session state
    page_options = ["🏠 Home", "📈 Forecast", "ℹ️ About", "📞 Contact"]
    index = page_options.index(st.session_state.page)
    
    st.session_state.page = st.radio(
        "Navigation",
        page_options,
        index=index
    )

# Route to pages
if st.session_state.page == "🏠 Home":
    from app.pages.home import show_home
    show_home()
elif st.session_state.page == "📈 Forecast":
    from app.pages.forecast import show_forecast
    show_forecast()
elif st.session_state.page == "ℹ️ About":
    from app.pages.about import show_about
    show_about()
elif st.session_state.page == "📞 Contact":
    from app.pages.contact import show_contact
    show_contact()