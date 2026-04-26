# pages/contact.py
import streamlit as st
from app.config import THEME, BRAND_NAME
from app.ui_components import render_hero, render_section_header

def show_contact():
    # Standard Hero
    render_hero(
        title="Get in Touch",
        subtitle="Whether you have a technical question, a partnership proposal, or just want to share feedback — we're listening."
    )

    col1, col2 = st.columns([1.6, 1.4], gap="large")

    with col1:
        render_section_header("✉️", "Direct Signal", color=THEME['secondary'])
        st.write("Fill out the form below and I'll receive it instantly.")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name", placeholder="Enter your name")
            email = st.text_input("Email Address", placeholder="name@company.com")
            
            inquiry_type = st.selectbox(
                "Inquiry Category",
                ["General Inquiry", "Algorithm & Model Feedback", "Academic Collaboration", 
                 "Data Licensing", "Feature Request", "Report a Bug"]
            )
            
            message = st.text_area("Your Message", placeholder="How can I help you?", height=200)
            
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("SEND", use_container_width=True, type="primary")
            
            if submitted:
                if not name or not email or not message.strip():
                    st.error("⚠️ All fields are required to establish a connection.")
                elif "@" not in email:
                    st.error("⚠️ Please provide a valid email address.")
                else:
                    st.balloons()
                    st.success("✅ **Transmission Successful!** Your message has been sent to the developer.")

    with col2:
        render_section_header("👤", "Developer Profile", color=THEME['secondary'])
        
        st.markdown(f"""<div style="background: {THEME['sidebar']}; padding: 2.5rem; border-radius: 28px; border: 1px solid rgba(255,255,255,0.05); border-top: 5px solid {THEME['secondary']}; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1.5rem;">
<div style="background: {THEME['primary']}; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: 900;">CD</div>
<div>
<h3 style="margin: 0; color: white; font-weight: 800;">Chimbueze David</h3>
<p style="margin: 0; color: #E2E8F0; font-size: 0.9rem;">Lead Developer, NairaPulse AI</p>
</div>
</div>
<p style="color: #E2E8F0; line-height: 1.6; font-size: 0.95rem;">
Final Year Student, Department of Computing<br>
<b>Afe Babalola University, Ado-Ekiti</b>
</p>
<hr style="margin: 2rem 0; border: 0.5px solid rgba(255,255,255,0.1);">
<div style="display: flex; flex-direction: column; gap: 15px;">
<a href="https://github.com/ChimbuezeDavid" target="_blank" style="text-decoration: none;">
<div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); color: white; display: flex; align-items: center; gap: 12px;">
<span>💻</span> <b>GitHub Profile</b>
</div>
</a>
<a href="https://x.com/ChimbuezeDavid" target="_blank" style="text-decoration: none;">
<div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); color: white; display: flex; align-items: center; gap: 12px;">
<span>𝕏</span> <b>Twitter / X</b>
</div>
</a>
</div>
<div style="margin-top: 2rem; padding: 1rem; background: rgba(59, 130, 246, 0.1); border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.2);">
<p style="margin: 0; font-size: 0.85rem; color: #93c5fd;">
🕒 <b>Response Time:</b><br>
Typically responds within 24-48 business hours.
</p>
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Collaborative Details Section - Using standardized dark cards
    render_section_header("🤝", "Why Collaborate?", color=THEME['secondary'])
    
    col_a, col_b, col_c = st.columns(3)
    
    from app.ui_components import render_card
    with col_a:
        render_card("🔍 Research", "Exchange insights on stacked ensemble methodologies and time-series econometrics.", color=THEME['secondary'], height="250px")
    
    with col_b:
        render_card("🏢 Industry", "Discuss how these forecasts can integrate into corporate supply chain or pricing strategies.", color=THEME['secondary'], height="250px")
    
    with col_c:
        render_card("🛠️ Improvement", "Suggest new features, macro indicators, or structural break detections for future versions.", color=THEME['secondary'], height="250px")


if __name__ == "__main__":
    show_contact()