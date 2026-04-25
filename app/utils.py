# app/utils.py
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

def calculate_implied_index(current_index: float, mom_pct: float) -> float:
    """Calculate new CPI index after applying MoM change"""
    return current_index * (1 + mom_pct / 100)

def create_forecast_chart(dates, mom_values, category: str):
    """Create interactive Plotly chart for forecast"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=mom_values,
        mode='lines+markers',
        name='Predicted MoM %',
        line=dict(color='#10B981', width=3),
        marker=dict(size=8, color='#F97316')
    ))
    
    fig.update_layout(
        title=f"{category} - Forecasted Month-over-Month % Change",
        xaxis_title="Month",
        yaxis_title="MoM % Change (%)",
        template="plotly_white",
        height=480,
        hovermode="x unified"
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.6)
    return fig