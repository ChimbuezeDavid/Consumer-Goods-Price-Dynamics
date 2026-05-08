# app/utils.py
"""
NairaPulse AI - Utility Functions
Visualization helpers with consistent professional styling.
"""

import pandas as pd
import plotly.graph_objects as go


def create_forecast_chart(dates: pd.DatetimeIndex, mom_values: list, category: str, theme: dict):
    """
    Clean 2D line chart with consistent professional color.
    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=mom_values,
        mode='lines+markers',
        name='MoM % Change',
        line=dict(color=theme['primary'], width=3.5),
        marker=dict(
            size=7,
            color=theme['primary'],
            line=dict(width=1.5, color=theme['surface'])
        ),
        hovertemplate="%{x|%b %Y}<br><b>MoM: %{y:+.2f}%</b><extra></extra>"
    ))

    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color=theme['muted'], 
        line_width=1
    )

    fig.update_layout(
        title=dict(
            text=f"{category} — Projected Monthly Price Changes",
            font=dict(size=18, color=theme['primary'], family="Inter"),
            x=0.02
        ),
        xaxis=dict(
            title="Forecast Period",
            showgrid=True,
            gridcolor=theme['border'],
            tickfont=dict(size=11, family="Inter", color=theme['muted'])
        ),
        yaxis=dict(
            title="Month-over-Month Change (%)",
            showgrid=True,
            gridcolor=theme['border'],
            tickfont=dict(size=11, family="Inter", color=theme['muted'])
        ),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=40),
        height=420,
        hovermode="x unified"
    )

    return fig