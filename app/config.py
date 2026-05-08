# app/config.py
"""
NairaPulse AI - Configuration (Light Theme Only)
"""

from pathlib import Path
from app.colors import THEME

BASE_DIR = Path(__file__).parent.parent

LAST_KNOWN_CPI = {
    "Food": 783.0,
    "Transport": 552.81,
    "Clothing And Footwear": 512.54
}

BRAND_NAME = "NairaPulse AI"

PAGE_CONFIG = {
    "page_title": f"{BRAND_NAME} | Nigeria Price Dynamics",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS - Light Theme + Improved Buttons & Responsiveness
# ─────────────────────────────────────────────────────────────────────────────
def get_custom_css(theme):
    return f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {{
    --np-primary: {theme['primary']};
    --np-accent: {theme['accent']};
    --np-success: {theme['success']};
    --np-danger: {theme['danger']};
    --np-bg: {theme['background']};
    --np-surface: {theme['surface']};
    --np-sidebar: {theme['sidebar']};
    --np-text: {theme['text']};
    --np-muted: {theme['muted']};
    --np-border: {theme['border']};
}}

.stApp {{ background-color: var(--np-bg); color: var(--np-text); }}

.np-hero {{ 
    background: var(--np-surface); 
    padding: 3.8rem 2.8rem; 
    border-bottom: 4px solid var(--np-primary);
    margin: -1rem -1rem 3rem -1rem;
    border-radius: 0 0 12px 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}}
.np-hero-title {{ font-size: 3.1rem; font-weight: 800; color: var(--np-primary); }}
.np-hero-subtitle {{ font-size: 1.25rem; color: var(--np-muted); }}

.np-card {{
    background: var(--np-surface);
    border: 1px solid var(--np-border);
    border-radius: 12px;
    padding: 1.8rem;
    height: 100%;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}}
.np-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.1);
}}

/* Premium Buttons */
.stButton > button {{
    background: linear-gradient(135deg, var(--np-accent), #9C3F00);
    color: white !important;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    border-radius: 12px;
    padding: 0.7rem 2.5rem;
    border: none;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 4px 15px rgba(180, 83, 9, 0.25);
    width: 100%;
}}

.stButton > button:hover {{
    background: linear-gradient(135deg, #9C3F00, var(--np-accent));
    box-shadow: 0 8px 25px rgba(180, 83, 9, 0.45);
    transform: translateY(-3px) scale(1.02);
}}

.stButton > button:active {{
    transform: translateY(0) scale(0.98);
}}

/* Chat UI Improvements - Glassmorphism */
[data-testid="stChatMessage"] {{
    background-color: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(10px);
    border: 1px solid var(--np-border) !important;
    border-radius: 20px !important;
    padding: 1.2rem !important;
    margin-bottom: 1.2rem !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}}

/* User Message specific */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{
    border-right: 4px solid var(--np-primary) !important;
}}

/* Assistant Message specific */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {{
    border-left: 4px solid var(--np-accent) !important;
}}

[data-testid="stChatMessageAvatarUser"] {{
    background-color: var(--np-primary) !important;
    border-radius: 50% !important;
}}

[data-testid="stChatMessageAvatarAssistant"] {{
    background-color: var(--np-accent) !important;
    border-radius: 50% !important;
}}

/* Sidebar Styling */
section[data-testid="stSidebar"] {{
    background-color: var(--np-sidebar);
    border-right: 1px solid var(--np-border);
}}

/* Inputs */
.stTextInput > div > div > input, .stTextArea > div > div > textarea {{
    background-color: var(--np-surface) !important;
    color: var(--np-text) !important;
    border: 1px solid var(--np-border) !important;
    border-radius: 8px !important;
}}

/* Mobile Responsiveness */
@media (max-width: 768px) {{
    .np-hero {{ padding: 2.5rem 1.5rem; }}
    .np-hero-title {{ font-size: 2.4rem; }}
}}
</style>"""


