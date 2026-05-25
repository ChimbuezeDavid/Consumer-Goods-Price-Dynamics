# app/config.py
"""
NairaPulse AI - Enhanced Configuration
Improved CSS with better formatting, animations, and responsive design.
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
    "initial_sidebar_state": "auto"
}

def get_custom_css(theme):
    return f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
@import url('https://cdn.jsdelivr.net/npm/icofont@1.0.0/dist/icofont.min.css');

/* IcoFont icon sizing utilities */
.np-icon-sm  {{ font-size: 1.1rem; }}
.np-icon-md  {{ font-size: 1.6rem; }}
.np-icon-lg  {{ font-size: 2.2rem; }}
.np-icon-xl  {{ font-size: 3rem;   }}
.np-icon-primary {{ color: var(--np-primary); }}
.np-icon-accent  {{ color: var(--np-accent);  }}
.np-icon-muted   {{ color: var(--np-muted);   }}
.np-icon-white   {{ color: #ffffff;            }}

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

/* Global Styles */
.stApp {{ 
    background-color: var(--np-bg); 
    color: var(--np-text);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}}

/* Hero Section */
.np-hero {{ 
    background: linear-gradient(135deg, var(--np-surface) 0%, var(--np-sidebar) 100%);
    padding: 3.8rem 2.8rem; 
    border-bottom: 4px solid var(--np-primary);
    margin: -1rem -1rem 3rem -1rem;
    border-radius: 0 0 16px 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}}

.np-hero-title {{ 
    font-size: 3.2rem; 
    font-weight: 900; 
    color: var(--np-primary); 
    line-height: 1.1;
    margin-bottom: 1rem;
}}

.np-hero-subtitle {{ 
    font-size: 1.3rem; 
    color: var(--np-muted); 
    font-weight: 500;
    line-height: 1.6;
}}

/* Section Headers */
.np-section-header {{
    font-size: 2rem;
    font-weight: 800;
    color: var(--np-primary);
    margin: 3rem 0 1.5rem 0;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    border-bottom: 2px solid var(--np-border);
    padding-bottom: 0.8rem;
}}

/* Cards */
.np-card {{
    background: var(--np-surface);
    border: 1px solid var(--np-border);
    border-radius: 16px;
    padding: 2rem;
    height: 100%;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}}

.np-card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
    border-color: var(--np-primary);
}}

.np-card-title {{
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--np-primary);
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}

.np-card-body {{
    color: var(--np-text);
    line-height: 1.8;
    font-size: 0.95rem;
}}

.uniform-card {{
    height: 100%;
    display: flex;
    flex-direction: column;
}}

/* Buttons - Premium Style */
.stButton > button {{
    background: linear-gradient(135deg, var(--np-accent) 0%, #C5630D 100%);
    color: white !important;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    border-radius: 12px;
    padding: 0.85rem 2.5rem;
    border: none;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 14px rgba(180, 83, 9, 0.3);
    font-size: 0.9rem;
    width: 100%;
}}

.stButton > button:hover {{
    background: linear-gradient(135deg, #C5630D 0%, var(--np-accent) 100%);
    box-shadow: 0 6px 20px rgba(180, 83, 9, 0.4);
    transform: translateY(-2px);
}}

.stButton > button:active {{
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(180, 83, 9, 0.3);
}}

/* Download Button Specific */
.stDownloadButton > button {{
    background: linear-gradient(135deg, var(--np-success) 0%, #059669 100%);
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}}

.stDownloadButton > button:hover {{
    background: linear-gradient(135deg, #059669 0%, var(--np-success) 100%);
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}}

/* Form Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {{
    background-color: var(--np-surface) !important;
    color: var(--np-text) !important;
    border: 2px solid var(--np-border) !important;
    border-radius: 10px !important;
    padding: 0.75rem !important;
    font-size: 0.95rem !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {{
    border-color: var(--np-accent) !important;
    box-shadow: 0 0 0 3px rgba(180, 83, 9, 0.15) !important;
    outline: none !important;
}}

/* Selectbox — target the wrapper, not the inner div, to avoid splitting the widget */
.stSelectbox > label {{
    color: var(--np-text) !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    margin-bottom: 0.3rem !important;
}}

[data-baseweb="select"] > div:first-child {{
    background-color: var(--np-surface) !important;
    border: 2px solid var(--np-border) !important;
    border-radius: 10px !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}

[data-baseweb="select"] > div:first-child:hover {{
    border-color: var(--np-accent) !important;
}}

[data-baseweb="select"] > div:first-child:focus-within {{
    border-color: var(--np-accent) !important;
    box-shadow: 0 0 0 3px rgba(180, 83, 9, 0.15) !important;
}}

[data-baseweb="select"] span,
[data-baseweb="select"] div {{
    color: var(--np-text) !important;
}}

/* Select dropdown menu */
[data-baseweb="popover"] [data-baseweb="menu"] {{
    background-color: var(--np-surface) !important;
    border: 1px solid var(--np-border) !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12) !important;
}}

[data-baseweb="menu"] li:hover,
[data-baseweb="option"]:hover {{
    background-color: var(--np-sidebar) !important;
    color: var(--np-accent) !important;
}}

/* Sliders */
.stSlider > div > div > div > div {{
    background-color: var(--np-primary) !important;
}}

.stSlider > div > div > div {{
    background-color: var(--np-border) !important;
}}

/* Expanders */
.streamlit-expanderHeader {{
    background-color: var(--np-surface);
    border: 1px solid var(--np-border);
    border-radius: 10px;
    padding: 1rem !important;
    font-weight: 600 !important;
    color: var(--np-primary) !important;
    transition: all 0.2s ease;
}}

.streamlit-expanderHeader:hover {{
    background-color: var(--np-sidebar);
    border-color: var(--np-primary);
}}

/* Dataframes */
.stDataFrame {{
    border: 1px solid var(--np-border);
    border-radius: 12px;
    overflow: hidden;
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background-color: var(--np-sidebar);
    border-right: 2px solid var(--np-border);
}}

section[data-testid="stSidebar"] > div {{
    padding-top: 2rem;
}}

/* Metrics */
[data-testid="stMetricValue"] {{
    font-size: 2rem;
    font-weight: 800;
    color: var(--np-primary);
}}

[data-testid="stMetricLabel"] {{
    font-size: 0.9rem;
    color: var(--np-muted);
    font-weight: 600;
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 0.5rem;
    background-color: var(--np-surface);
    padding: 0.5rem;
    border-radius: 12px;
}}

.stTabs [data-baseweb="tab"] {{
    height: 50px;
    background-color: transparent;
    border-radius: 10px;
    color: var(--np-muted);
    font-weight: 600;
    padding: 0 1.5rem;
    transition: all 0.2s ease;
}}

.stTabs [data-baseweb="tab"]:hover {{
    background-color: var(--np-sidebar);
}}

.stTabs [aria-selected="true"] {{
    background-color: var(--np-primary) !important;
    color: white !important;
}}

/* Info/Success/Warning/Error Boxes */
.stAlert {{
    border-radius: 12px;
    border-left-width: 4px;
    padding: 1.2rem 1.5rem;
    font-size: 0.95rem;
}}

/* Code Blocks */
.stCodeBlock {{
    border-radius: 10px;
    border: 1px solid var(--np-border);
}}

/* Progress Bar */
.stProgress > div > div > div > div {{
    background-color: var(--np-primary);
}}

/* Spinner */
.stSpinner > div {{
    border-top-color: var(--np-primary) !important;
}}

/* Links */
a {{
    color: var(--np-primary);
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s ease;
}}

a:hover {{
    color: var(--np-accent);
    text-decoration: underline;
}}

/* Scrollbar */
::-webkit-scrollbar {{
    width: 10px;
    height: 10px;
}}

::-webkit-scrollbar-track {{
    background: var(--np-bg);
}}

::-webkit-scrollbar-thumb {{
    background: var(--np-border);
    border-radius: 5px;
}}

::-webkit-scrollbar-thumb:hover {{
    background: var(--np-muted);
}}

/* Tooltip */
[data-testid="stTooltipIcon"] {{
    color: var(--np-muted);
}}

/* Mobile Responsive - Enhanced Visibility */
@media (max-width: 768px) {{
    .stApp p, .stApp li {{
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }}

    .np-hero {{ 
        padding: 2.5rem 1.5rem; 
    }}
    
    .np-hero-title {{ 
        font-size: 2.5rem; 
    }}
    
    .np-hero-subtitle {{
        font-size: 1.25rem;
    }}
    
    .np-section-header {{
        font-size: 1.8rem;
    }}
    
    .np-card {{
        padding: 1.5rem;
    }}
    
    .stButton > button {{
        font-size: 1rem;
        padding: 0.8rem 1.5rem;
    }}
    
    .stat-value {{
        font-size: 2.2rem !important;
    }}
    
    [data-testid="stMetricValue"] {{
        font-size: 2rem !important;
    }}
}}

/* Animation Classes */
@keyframes fadeIn {{
    from {{
        opacity: 0;
        transform: translateY(10px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.fade-in {{
    animation: fadeIn 0.5s ease-out;
}}

/* Highlight Box */
.highlight-box {{
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.05), rgba(180, 83, 9, 0.05));
    border-left: 4px solid var(--np-accent);
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1.5rem 0;
}}

/* Stats Grid */
.stats-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}}

.stat-card {{
    background: var(--np-surface);
    border: 1px solid var(--np-border);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
}}

.stat-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}}

.stat-value {{
    font-size: 2.5rem;
    font-weight: 900;
    color: var(--np-primary);
    margin: 0.5rem 0;
}}

.stat-label {{
    font-size: 0.9rem;
    color: var(--np-muted);
    font-weight: 600;
}}

/* Badge */
.badge {{
    display: inline-block;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    background: var(--np-primary);
    color: white;
}}

.badge-success {{
    background: var(--np-success);
}}

.badge-warning {{
    background: var(--np-accent);
}}

.badge-danger {{
    background: var(--np-danger);
}}

/* Hide Streamlit Default Elements & Cloud Viewer Badge */
#MainMenu {{visibility: hidden !important;}}
#GithubIcon {{visibility: hidden !important;}}
footer {{visibility: hidden !important;}}

.viewerBadge_container__1QSob,
.viewerBadge_container__3yXjG,
[class^="viewerBadge_container"],
[class*="viewerBadge"],
#viewerBadge_container,
.stDeployButton,
[data-testid="stAppDeployButton"],
iframe[src*="badge"] {{
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
}}

/* Hide specific toolbar chrome — NOT the header/toolbar wrapper itself */
[data-testid="stToolbarActions"] {{
    display: none !important;
}}
[data-testid="stDecoration"] {{
    display: none !important;
}}
[data-testid="stStatusWidget"] {{
    display: none !important;
}}

/* Keep header transparent but keep its layout so hamburger stays clickable */
header[data-testid="stHeader"] {{
    background: transparent !important;
    pointer-events: none !important;
}}

/* Re-enable pointer events only on the hamburger button */
[data-testid="collapsedControl"] {{
    display: flex !important;
    visibility: visible !important;
    pointer-events: all !important;
    z-index: 9999 !important;
}}

[data-testid="collapsedControl"] svg,
[data-testid="collapsedControl"] span {{
    color: var(--np-primary) !important;
    fill: var(--np-primary) !important;
}}

/* Force Text Color on Streamlit Typography & Sidebar */
.stApp p, 
.stApp li, 
.stApp label,
.stApp [data-testid="stSidebarNav"] span,
.stApp [data-testid="stSidebarNav"] a {{
    color: var(--np-text) !important;
}}

/* Sidebar Navigation Hover & Active Background */
.stApp [data-testid="stSidebarNav"] a:hover,
.stApp [data-testid="stSidebarNav"] a[aria-current="page"] {{
    background-color: var(--np-surface) !important;
}}
</style>"""