import streamlit as st

def show_about():
    st.title("ℹ️ About This Project")

    st.markdown("""
    <div style='background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%); 
                color: white; padding: 3rem 2rem; border-radius: 20px; text-align: center; margin-bottom: 3rem;'>
        <h2 style='margin-bottom: 1rem;'>Nigeria CPI Forecaster</h2>
        <p style='font-size: 1.25rem; max-width: 700px; margin: 0 auto; opacity: 0.9;'>
            A powerful stacked ensemble forecasting tool for consumer price dynamics in Nigeria.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Project Overview")
        st.markdown("""
        This application forecasts **month-on-month percentage changes** in key Consumer Price Index (CPI) categories using a sophisticated **stacked ensemble model**.

        The system combines SARIMAX, Random Forest, and LSTM as base learners, with XGBoost acting as the meta-learner to optimally combine their predictions.
        """)

    with col2:
        st.markdown("### Technical Stack")
        st.markdown("""
        - **Base Models**: SARIMAX (with exogenous variables), Random Forest, LSTM  
        - **Meta-Learner**: XGBoost  
        - **Frontend**: Streamlit  
        - **Data**: NBS CPI series + macroeconomic indicators
        """)

    st.markdown("---")

    # Scope Section
    st.markdown("### Project Scope")
    st.markdown("""
    **Macroeconomic Variables Used:**
    - Inflation Rate
    - Exchange Rate (NGN/USD)
    - Crude Oil Price (USD per barrel)

    **CPI Categories Forecasted (Month-on-Month % Change):**
    - Food
    - Transport
    - Clothing and Footwear
    - Health
    - Housing, Water, Electricity, Gas and Other Fuel

    **Why these variables and categories?**

    Nigeria’s economy is heavily influenced by oil revenue, foreign exchange availability, and inflationary pressures. 
    Oil price affects government revenue and fuel costs, exchange rate impacts imported goods (especially food and raw materials), 
    while inflation rate serves as a broad indicator of price level changes. 

    These five CPI categories were chosen because they represent the **most essential** areas of household expenditure in Nigeria. 
    Food, Transport, and Housing/Utilities together make up a very large portion of the average Nigerian’s monthly spending, 
    making their price movements critical for businesses, policymakers, and households.
    """)

    st.markdown("---")

    st.markdown("### Academic Context")
    st.markdown("""
    This is a **Final Year Project** from the  
    **Department of Computing**,  
    **Afe Babalola University, Ado-Ekiti (ABUAD)**.

    The project demonstrates the practical application of machine learning and time series forecasting to address real economic challenges facing Nigeria.
    """)

    st.info("""
    **Note**: This tool is developed for educational and analytical purposes. Forecasts should be used alongside official data and expert economic judgment.
    """)