# app/ui_components.py
import streamlit as st
from app.config import THEME, BRAND_NAME

def render_hero(title, subtitle, icon="🇳🇬"):
    """Standard Premium Hero Section"""
    html = (
        f'<div style="background: linear-gradient(135deg, {THEME["primary"]} 0%, #1e3a8a 50%, #1e293b 100%); '
        f'padding: 5rem 2rem; border-radius: 35px; color: white; margin-bottom: 3.5rem; text-align: center; '
        f'box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25); position: relative; overflow: hidden; '
        f'border: 1px solid {THEME["secondary"]}30;">'
        f'<div style="position: absolute; top: 0; left: 0; right: 0; height: 100%; opacity: 0.1; background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 20px 20px;"></div>'
        f'<h1 style="font-size: 4.5rem; font-weight: 900; margin-bottom: 0.5rem; color: white; letter-spacing: -2px; line-height: 1;">{title}</h1>'
        f'<div style="height: 5px; width: 80px; background: {THEME["secondary"]}; margin: 1.5rem auto; border-radius: 5px;"></div>'
        f'<p style="font-size: 1.5rem; opacity: 0.9; max-width: 800px; margin: 1rem auto; font-weight: 300; line-height: 1.5;">{subtitle}</p>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)

def render_section_header(icon, title, color=None):
    """Standard Section Header with Gold Accent"""
    if color is None:
        color = THEME['secondary']
    st.markdown(f"<h2 class='gold-header' style='color: {color} !important; margin-top: 2rem; margin-bottom: 1.5rem;'>{icon} {title}</h2>", unsafe_allow_html=True)

def render_card(title, content, color=None, icon=None, height="320px"):
    """Standard Premium Glassmorphic Card"""
    if color is None:
        color = THEME['secondary']
    
    icon_html = f'<div style="font-size: 3.5rem; margin-bottom: 1.5rem; filter: drop-shadow(0 0 10px {color}40);">{icon}</div>' if icon else ""
    
    html = (
        f'<div style="background: {THEME["sidebar"]}; border: 1px solid rgba(255,255,255,0.05); '
        f'border-top: 5px solid {color}; border-radius: 28px; padding: 3rem 2rem; text-align: center; '
        f'height: {height}; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3); transition: all 0.3s ease;">'
        f'{icon_html}'
        f'<h3 style="margin: 0 0 1rem 0; color: white; font-weight: 800; font-size: 1.6rem; letter-spacing: -0.5px;">{title}</h3>'
        f'<div style="font-size: 1rem; color: #E2E8F0; line-height: 1.6; font-weight: 400;">{content}</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)

import textwrap

def render_sidebar_info_card(title, data):
    """Standard Sidebar Info Display"""
    items_html = ""
    for label, value in data.items():
        # Remove all leading whitespace from each item to prevent code-block triggering
        items_html += (
            f'<div style="margin-bottom: 1rem;">'
            f'<small style="color: #64748b; font-weight: 700;">{label.upper()}</small><br>'
            f'<span style="font-size: 1.4rem; font-weight: 800; color: {THEME["text"]};">{value}</span>'
            f'</div>'
        )
    
    # Construct the final HTML with zero indentation
    html = (
        f'<div style="background: {THEME["sidebar"]}; padding: 2.5rem; border-radius: 24px; '
        f'border: 1px solid rgba(255,255,255,0.05); '
        f'border-left: 8px solid {THEME["secondary"]}; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);">'
        f'<h4 style="margin-top: 0; color: {THEME["secondary"]} !important; margin-bottom: 1.5rem; font-weight: 800;">{title}</h4>'
        f'{items_html}'
        f'</div>'
    )
    
    st.markdown(html, unsafe_allow_html=True)
