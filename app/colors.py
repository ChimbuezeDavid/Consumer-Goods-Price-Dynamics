# app/colors.py
"""
NairaPulse AI - Premium Dual-Theme Color System
"""

# LIGHT THEME
LIGHT_PRIMARY    = "#0F172A"
LIGHT_ACCENT     = "#B45309"
LIGHT_SUCCESS    = "#10B981"
LIGHT_DANGER     = "#EF4444"
LIGHT_BACKGROUND = "#F8FAFC"
LIGHT_SURFACE    = "#FFFFFF"
LIGHT_SIDEBAR    = "#F1F5F9"
LIGHT_BORDER     = "#E2E8F0"
LIGHT_TEXT       = "#0F172A"
LIGHT_MUTED      = "#64748B"

# DARK THEME
DARK_PRIMARY     = "#38BDF8"
DARK_ACCENT      = "#F59E0B"
DARK_SUCCESS     = "#34D399"
DARK_DANGER      = "#F87171"
DARK_BACKGROUND  = "#020617"
DARK_SURFACE     = "#0F172A"
DARK_SIDEBAR     = "#1E293B"
DARK_BORDER      = "#334155"
DARK_TEXT        = "#F1F5F9"
DARK_MUTED       = "#94A3B8"

def get_theme(dark_mode=False):
    if dark_mode:
        return {
            "primary": DARK_PRIMARY,
            "accent": DARK_ACCENT,
            "success": DARK_SUCCESS,
            "danger": DARK_DANGER,
            "background": DARK_BACKGROUND,
            "surface": DARK_SURFACE,
            "sidebar": DARK_SIDEBAR,
            "border": DARK_BORDER,
            "text": DARK_TEXT,
            "muted": DARK_MUTED,
        }
    return {
        "primary": LIGHT_PRIMARY,
        "accent": LIGHT_ACCENT,
        "success": LIGHT_SUCCESS,
        "danger": LIGHT_DANGER,
        "background": LIGHT_BACKGROUND,
        "surface": LIGHT_SURFACE,
        "sidebar": LIGHT_SIDEBAR,
        "border": LIGHT_BORDER,
        "text": LIGHT_TEXT,
        "muted": LIGHT_MUTED,
    }

# Default theme for static imports (deprecated, use get_theme)
THEME = get_theme(False)
CHART_LINE = LIGHT_PRIMARY