# app/utils.py
"""
NairaPulse AI - Utility Functions
Updated with better chart colors and cleaner styling.
"""

import pandas as pd
import plotly.graph_objects as go


def create_forecast_chart(dates: pd.DatetimeIndex, mom_values: list, category: str, theme: dict):
    """
    Professional chart with theme-aware primary color line.
    """
    fig = go.Figure()

    # Determine marker colors based on direction (Green for upward/positive, Red for downward/negative)
    marker_colors = [theme['success'] if val > 0 else theme['danger'] for val in mom_values]

    fig.add_trace(go.Scatter(
        x=dates,
        y=mom_values,
        mode='lines+markers',
        name='MoM % Change',
        line=dict(color=theme['primary'], width=3),
        marker=dict(
            size=10,
            color=marker_colors,
            line=dict(width=2, color=theme['surface'])
        ),
        hovertemplate="<b>%{x|%b %Y}</b><br>MoM: %{y:+.2f}%<extra></extra>"
    ))

    # Zero reference line
    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color=theme['muted'], 
        line_width=1.5,
        opacity=0.5
    )

    fig.update_layout(
        title=dict(
            text=f"{category} — Projected Monthly Changes",
            font=dict(size=20, color=theme['primary'], family="Inter"),
            x=0.02,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Forecast Period", font=dict(size=14, color=theme['text'])),
            showgrid=True,
            gridcolor=theme['border'],
            gridwidth=1,
            tickfont=dict(size=12, family="Inter", color=theme['muted'])
        ),
        yaxis=dict(
            title=dict(text="Month-over-Month Change (%)", font=dict(size=14, color=theme['text'])),
            showgrid=True,
            gridcolor=theme['border'],
            gridwidth=1,
            tickfont=dict(size=12, family="Inter", color=theme['muted'])
        ),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=60, r=40, t=80, b=60),
        height=450,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor=theme['surface'],
            font_size=13,
            font_family="Inter"
        )
    )

    return fig