# app/ui_components.py
"""
NairaPulse AI - Reusable UI Components
Clean, professional components optimized for light theme.
"""

import streamlit as st

def render_hero(title: str, subtitle: str):
    """Authoritative hero section."""
    st.markdown(f"""
    <div class="np-hero">
        <div class="np-hero-title">{title}</div>
        <div class="np-hero-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def render_section_header(icon_html: str, title: str):
    """Consistent section headers. icon_html can be an IcoFont <i> tag or plain text."""
    st.markdown(f"""
    <div class="np-section-header">
        <span style="font-size:1.9rem; display:inline-flex; align-items:center;">{icon_html}</span> {title}
    </div>
    """, unsafe_allow_html=True)

def render_card(title: str, content: str, icon: str = None):
    """Standard content card with uniform height support."""
    icon_html = f'<span style="margin-right:0.6rem; font-size:1.6rem;">{icon}</span>' if icon else ''
    st.markdown(f"""
    <div class="np-card">
        <div class="np-card-title">{icon_html}{title}</div>
        <div class="np-card-body">{content}</div>
    </div>
    """, unsafe_allow_html=True)

def render_metric_card(label: str, value: str, color: str = "var(--np-primary)"):
    """Metric cards with optional custom value color."""
    st.markdown(f"""
    <div class="np-card" style="text-align:center; height:100%;">
        <div style="font-size:0.95rem; color:var(--np-muted); margin-bottom:0.6rem;">{label}</div>
        <div style="font-size:2.25rem; font-weight:800; color:{color};">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def render_tech_badge(name: str, subtitle: str):
    """Technology badge for home page."""
    st.markdown(f"""
    <div class="np-card" style="text-align:center; padding:1.4rem 1rem;">
        <div style="font-weight:700; font-size:1.1rem; color:var(--np-primary);">{name}</div>
        <div style="color:var(--np-muted); font-size:0.9rem; margin-top:0.4rem;">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)