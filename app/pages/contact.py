# pages/contact.py
"""
NairaPulse AI - Contact & Feedback Page
Clean, professional contact form with full dark mode support.
"""

import streamlit as st
from app.colors import THEME
from app.ui_components import render_hero, render_section_header, render_card

def show_contact():
    """Render contact page with message form and project information."""
    render_hero(
        title="Contact & Collaboration",
        subtitle="We welcome your feedback, questions, and ideas. Help us improve economic intelligence tools for Nigeria."
    )

    col1, col2 = st.columns([1.65, 1], gap="large")

    with col1:
        render_section_header("✉️", "Send a Message")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name", placeholder="Chinedu Okoro")
            email = st.text_input("Email Address", placeholder="you@example.com")
            
            topic = st.selectbox(
                "Topic",
                ["General Inquiry", "Research Collaboration", "Technical Feedback", 
                 "Bug Report", "Feature Suggestion", "Academic Partnership"]
            )
            
            message = st.text_area("Your Message", height=180, 
                                 placeholder="I would like to discuss potential collaboration...")
            
            submitted = st.form_submit_button("SEND MESSAGE", use_container_width=True)
            
            if submitted:
                if name and email and message.strip():
                    st.success("✅ Thank you! Your message has been received. We'll respond shortly.")
                else:
                    st.error("Please fill in all required fields.")

    with col2:
        render_section_header("👤", "Project Details")
        
        st.markdown(f"""
        **Developer:** Chimbueze David  
        **Institution:** Afe Babalola University (ABUAD)  
        **Department:** Computing  
        **Year:** 2026
        """)

        st.markdown("---")

        render_card(
            title="Professional Links",
            content=f"""
            <a href="https://github.com/ChimbuezeDavid" target="_blank" style="color:inherit; text-decoration:none;">
                🔗 GitHub Profile
            </a><br><br>
            <a href="https://x.com/ChimbuezeDavid" target="_blank" style="color:inherit; text-decoration:none;">
                🔗 X / Twitter
            </a>
            """,
            icon="🔗"
        )

if __name__ == "__main__":
    show_contact()