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

# Financial Theme Colors
THEME = {
    "primary": "#1E40AF",    # Trust Blue
    "secondary": "#FBBF24",  # Gold
    "success": "#10B981",    # Emerald Green
    "danger": "#EF4444",     # Rose Red
    "background": "#F8FAFC", # Light Slate
    "sidebar": "#1E293B",    # Dark Slate
    "text": "#0F172A"        # Deep Navy
}

PAGE_CONFIG = {
    "page_title": f"{BRAND_NAME} | Nigeria Price Dynamics",
    "page_icon": "📉",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

CUSTOM_CSS = f"""
<style>
    .main {{
        background-color: {THEME['background']};
    }}
    .stButton>button {{
        background-color: {THEME['primary']};
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {THEME['secondary']};
        color: {THEME['text']};
        transform: translateY(-2px);
    }}
    [data-testid="stSidebar"] {{
        background-color: {THEME['sidebar']};
    }}
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
    h1, h2, h3 {{
        color: {THEME['primary']};
        font-family: 'Inter', sans-serif;
    }}
    .stMetric {{
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        border-left: 5px solid {THEME['primary']};
    }}
</style>
"""