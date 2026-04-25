# pages/contact.py
import streamlit as st
from app.config import THEME

def show_contact():
    # Modern Minimalist Header
    st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 20px; border-left: 10px solid {THEME['secondary']}; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 2rem;">
            <h1 style="color: {THEME['text']}; margin: 0; font-weight: 800;">Contact & Collaboration</h1>
            <p style="color: #64748b; font-size: 1.1rem; margin-top: 0.5rem;">Connect with <b>Chimbueze David</b> for insights or inquiries.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown(f"### <span style='color: {THEME['primary']}'>📬 Send a Signal</span>", unsafe_allow_html=True)
        with st.form("contact_form_v4"):
            st.text_input("Name")
            st.text_input("Email")
            st.selectbox("Inquiry Type", ["Data Inquiry", "Algorithm Feedback", "Partnership", "General"])
            st.text_area("Your Message")
            
            submitted = st.form_submit_button("SUBMIT PULSE")
            if submitted:
                st.success("Pulse transmitted. Thank you for reaching out.")

    with col2:
        st.markdown(f"### <span style='color: {THEME['primary']}'>🌐 Social Pulse</span>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: #F8FAFC; padding: 2rem; border-radius: 20px; border: 1px solid #E2E8F0;">
                <p style="margin-bottom: 1.5rem; color: #475569;"><b>Developer:</b> Chimbueze David</p>
                
                <a href="https://github.com/ChimbuezeDavid" style="text-decoration: none;">
                    <div style="background: white; padding: 0.8rem; border-radius: 12px; margin-bottom: 1rem; border: 1px solid #CBD5E1; color: {THEME['primary']}; display: flex; align-items: center; gap: 10px;">
                         GitHub Profile
                    </div>
                </a>
                
                <a href="https://x.com/ChimbuezeDavid" style="text-decoration: none;">
                    <div style="background: white; padding: 0.8rem; border-radius: 12px; border: 1px solid #CBD5E1; color: {THEME['primary']}; display: flex; align-items: center; gap: 10px;">
                         Twitter / X
                    </div>
                </a>
                
                <hr style="margin: 2rem 0;">
                <p style="font-size: 0.9rem; color: #64748b; text-align: center;">Lagos, Nigeria • ABUAD Computing</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_contact()