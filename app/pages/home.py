import streamlit as st

def show_home():
    # Dynamic Hero
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); 
                color: white; padding: 4.5rem 2rem; border-radius: 20px; text-align: center; margin-bottom: 3rem;'>
        <h1 style='font-size: 3.6rem; margin-bottom: 1rem; font-weight: 700; letter-spacing: -1px;'>
            🇳🇬 CPI Forecaster
        </h1>
        <p style='font-size: 1.55rem; max-width: 820px; margin: 0 auto 2.5rem auto; opacity: 0.95; line-height: 1.4;'>
            Understand how inflation, exchange rates, and oil prices shape consumer goods prices
        </p>
        <div style='display: inline-flex; gap: 12px; font-size: 1.1rem; background: rgba(255,255,255,0.15); padding: 14px 32px; border-radius: 50px;'>
            SARIMAX • Random Forest • LSTM • XGBoost
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2.8, 1.2])

    with col1:
        st.markdown("### Why This Tool Matters")
        st.markdown("""
        Nigeria’s consumer prices are highly sensitive to macroeconomic forces. 
        
        This forecaster uses a **stacked ensemble model** to predict **month-on-month price shifts** across major categories, helping you anticipate changes with confidence.
        """)

    with col2:
        st.info("""
        **Current Rates (April 2026)**
        - Core Inflation: **15.88%**
        - Exchange Rate: **₦1,356.89 / USD**
        - Oil Price: **$95.20 / barrel**
        """)

    st.markdown("---")

    # ==================== PERFECTLY BALANCED CATEGORIES ====================
    st.markdown("### Categories We Forecast")

    cat_data = [
        {"emoji": "🍲", "name": "Food", "color": "#FF6B6B"},
        {"emoji": "🚌", "name": "Transport", "color": "#4ECDC4"},
        {"emoji": "👕", "name": "Clothing & Footwear", "color": "#45B7D1"},
        {"emoji": "🏥", "name": "Health", "color": "#96CEB4"},
        {"emoji": "🏠", "name": "Housing & Utilities", "color": "#FFEEAD"}
    ]

    # Use equal-width columns with fixed height cards
    cols = st.columns(5)

    for i, cat in enumerate(cat_data):
        with cols[i]:
            st.markdown(f"""
            <div style='background: linear-gradient(145deg, {cat["color"]}15, #0F172A); 
                        border: 2px solid {cat["color"]}; 
                        border-radius: 16px; 
                        padding: 2rem 1.2rem; 
                        text-align: center; 
                        height: 260px;          /* Fixed height for perfect balance */
                        display: flex; 
                        flex-direction: column; 
                        justify-content: center; 
                        align-items: center;'>
                <div style='font-size: 3.4rem; margin-bottom: 1.2rem;'>{cat["emoji"]}</div>
                <h3 style='margin: 0 0 0.8rem 0; color: {cat["color"]}; font-weight: 600; font-size: 1.25rem;'>
                    {cat["name"]}
                </h3>
                <p style='margin: 0; font-size: 0.95rem; color: #94A3B8; line-height: 1.4;'>
                    Monthly price shift prediction
                </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Strong CTA
    st.markdown("""
    <div style='text-align: center; padding: 3.5rem 2rem; background: linear-gradient(90deg, #1E40AF, #3B82F6); 
                color: white; border-radius: 20px; margin: 2.5rem 0;'>
        <h2 style='margin-bottom: 1.2rem;'>Ready to simulate future price movements?</h2>
        <p style='font-size: 1.25rem; margin-bottom: 2rem; opacity: 0.92;'>
            Go to the Forecast page and adjust inflation, exchange rate, and oil price to see their impact.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Advanced Stacked Ensemble Forecasting • SARIMAX • Random Forest • LSTM • XGBoost")