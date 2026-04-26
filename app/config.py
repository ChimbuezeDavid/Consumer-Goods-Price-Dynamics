# app/config.py
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

LAST_KNOWN_CPI = {
    "Food": 783.0,
    "Transport": 552.81,
    "Clothing And Footwear": 512.54
}

# New Brand: NairaPulse AI
BRAND_NAME = "NairaPulse AI"

# Financial Theme Colors - High-End Dark Palette
THEME = {
    "primary": "#1D4ED8",    # Institutional Blue
    "secondary": "#FBBF24",  # Gold
    "success": "#10B981",    # Emerald Green
    "danger": "#EF4444",     # Rose Red
    "background": "#020617", # Ultra-Navy (Deepest)
    "sidebar": "#0F172A",    # Midnight Navy
    "text": "#F8FAFC"        # Off-White
}

PAGE_CONFIG = {
    "page_title": f"{BRAND_NAME} | Nigeria Price Dynamics",
    "page_icon": "📉",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

CUSTOM_CSS = f"""
<style>
    /* Global Page Styling - Aggressive Override */
    [data-testid="stAppViewContainer"] {{
        background-color: {THEME['background']} !important;
    }}
    [data-testid="stAppViewBlockContainer"] {{
        background-color: {THEME['background']} !important;
    }}
    .main {{
        background-color: {THEME['background']} !important;
    }}
    
    /* Global Text Styling */
    .main p, .main span, .main label, .main li, .main div {{
        color: {THEME['text']} !important;
    }}
    
    /* Header Overrides */
    h1, h2, h3, h4, h5, h6 {{
        color: white !important;
        font-family: 'Inter', sans-serif !important;
    }}
    
    /* Custom ID Overrides for Gold Headers */
    .gold-header {{
        color: {THEME['secondary']} !important;
    }}

    .stButton>button {{
        background-color: {THEME['primary']};
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }}
    .stMetric {{
        background-color: {THEME['sidebar']};
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255,255,255,0.05);
        border-left: 5px solid {THEME['primary']};
    }}
    /* Force metric text colors */
    [data-testid="stMetricValue"] > div {{
        color: white !important;
    }}
    [data-testid="stMetricLabel"] > div {{
        color: #E2E8F0 !important;
    }}
    /* High-Impact CTA Button */
    div#launch-cta .stButton>button {{
        background: linear-gradient(90deg, {THEME['secondary']} 0%, #F59E0B 100%);
        color: {THEME['text']};
        border: none;
        padding: 1.5rem 2rem;
        font-size: 1.5rem;
        font-weight: 900;
        letter-spacing: 2px;
        border-radius: 50px;
        box-shadow: 0 10px 20px rgba(251, 191, 36, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    div#launch-cta .stButton>button:hover {{
        transform: scale(1.05) translateY(-5px);
        box-shadow: 0 15px 30px rgba(251, 191, 36, 0.5);
        color: black;
    }}
</style>
"""