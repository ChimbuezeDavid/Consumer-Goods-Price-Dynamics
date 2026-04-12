import streamlit as st

def show_contact():
    st.title("📞 Contact & Feedback")

    st.markdown("""
    <div style='background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%); 
                color: white; padding: 3rem 2rem; border-radius: 20px; text-align: center; margin-bottom: 3rem;'>
        <h2 style='margin-bottom: 1rem;'>Get in Touch</h2>
        <p style='font-size: 1.2rem; opacity: 0.9;'>
            Have questions, suggestions, or interested in collaboration?
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Developer")
        st.markdown("""
        **Chimbueze David**  
        
        Final Year Student, Department of Computing  
        Afe Babalola University, Ado-Ekiti (ABUAD)
        
        - **GitHub**: [ChimbuezeDavid](https://github.com/ChimbuezeDavid)
        - **X (Twitter)**: [@ChimbuezeDavid](https://x.com/ChimbuezeDavid)
        """)

    with col2:
        st.markdown("### Feedback & Suggestions")
        st.markdown("""
        Your input is highly valuable. Feel free to reach out regarding:
        - Feature requests
        - UI/UX feedback  
        - Model improvements
        - Collaboration opportunities
        
        I’m always open to discussions on economic forecasting and machine learning applications in Nigeria.
        """)

    st.markdown("---")

    st.markdown("""
    ### Thank You
    This project was built with the goal of making advanced economic forecasting more accessible. 
    
    Thank you for using the Nigeria CPI Forecaster.
    """)

    st.caption("Built with ❤️ for Nigeria’s economic future")