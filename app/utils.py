import pandas as pd
import numpy as np
import plotly.graph_objects as go

def calculate_implied_index(current_index, mom_pct):
    return current_index * (1 + mom_pct / 100)

def create_forecast_chart(dates, mom_values, category):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=mom_values,
        mode='lines+markers',
        name='MoM % Change',
        line=dict(color='#FF4B4B', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=f"{category} - Predicted Month-on-Month % Change",
        xaxis_title="Month",
        yaxis_title="MoM % Change (%)",
        template="plotly_white",
        height=500,
        hovermode="x unified"
    )
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    return fig