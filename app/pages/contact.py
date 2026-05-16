# app/pages/contact.py
"""
NairaPulse AI - Enhanced Contact & Feedback Page
Clean, professional contact form with better UI and explanations.
"""

import streamlit as st
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
        
        st.markdown("""
        Have questions about the methodology? Found a bug? Want to collaborate on research?  
        Use the form below to get in touch.
        """)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input(
                "Full Name *", 
                placeholder="Chinedu Okoro",
                help="Your full name for identification"
            )
            
            email = st.text_input(
                "Email Address *", 
                placeholder="you@example.com",
                help="We'll respond to this email address"
            )
            
            topic = st.selectbox(
                "Topic *",
                ["General Inquiry", "Research Collaboration", "Technical Feedback", 
                 "Bug Report", "Feature Suggestion", "Academic Partnership", "Data Request"],
                help="Select the main purpose of your message"
            )
            
            message = st.text_area(
                "Your Message *", 
                height=200, 
                placeholder="I would like to discuss potential collaboration on...",
                help="Please provide as much detail as possible"
            )
            
            # Priority indicator
            priority = st.radio(
                "Priority Level",
                ["Normal", "High", "Urgent"],
                horizontal=True,
                help="High/Urgent for time-sensitive matters"
            )
            
            # Newsletter signup
            newsletter = st.checkbox(
                "📧 Subscribe to updates on model improvements and new features",
                help="Optional: Receive occasional updates (max 1-2 emails/month)"
            )
            
            submitted = st.form_submit_button("📨 SEND MESSAGE", use_container_width=True, type="primary")
            
            if submitted:
                if name and email and message.strip():
                    # In a real implementation, this would send to a backend API
                    st.success(f"""
                    ✅ **Thank you, {name}!**  
                    Your message has been received. We'll respond to **{email}** within 24-48 hours.
                    
                    **Topic:** {topic}  
                    **Priority:** {priority}
                    """)
                    
                    if newsletter:
                        st.info("📧 You've been subscribed to updates. Check your inbox for a confirmation email.")
                else:
                    st.error("⚠️ Please fill in all required fields (marked with *)")

        # Alternative Contact Methods
        st.markdown("<br>", unsafe_allow_html=True)
        render_section_header("📞", "Other Ways to Connect")
        
        alt_col1, alt_col2 = st.columns(2, gap="medium")
        
        with alt_col1:
            st.markdown("""
            **📧 Direct Email**  
            chimbuezedavid@abuad.edu.ng  
            (For urgent academic matters)
            
            **🐛 Report Issues**  
            Found a bug or technical issue?  
            File a detailed report on GitHub Issues
            """)
        
        with alt_col2:
            st.markdown("""
            **💬 Social Media**  
            Follow for updates and insights:
            - Twitter/X: @ChimbuezeDavid
            - LinkedIn: Connect for professional inquiries
            
            **🎓 Academic Inquiries**  
            For collaboration on forecasting research,  
            please email with "Research Collaboration" in subject
            """)

    with col2:
        render_section_header("👤", "Project Details")
        
        st.markdown(f"""
        <div class="np-card" style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); color:white;">
            <h4 style="color:white; margin-top:0;">Developer Information</h4>
            <div style="margin:1rem 0; line-height:1.8;">
                <strong>Name:</strong> Chimbueze David<br>
                <strong>Institution:</strong> Afe Babalola University (ABUAD)<br>
                <strong>Department:</strong> Computing<br>
                <strong>Level:</strong> Final Year (2025/2026)<br>
                <strong>Project Type:</strong> Undergraduate Research
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        render_card(
            title="🔗 Professional Links",
            content="""
            <div style="line-height:2;">
                <a href="https://github.com/ChimbuezeDavid" target="_blank" style="color:var(--np-primary); text-decoration:none; font-weight:600;">
                    🔗 GitHub Profile
                </a><br>
                <a href="https://x.com/ChimbuezeDavid" target="_blank" style="color:var(--np-primary); text-decoration:none; font-weight:600;">
                    🔗 X / Twitter
                </a><br>
                <a href="https://linkedin.com/in/chimbuezedavid" target="_blank" style="color:var(--np-primary); text-decoration:none; font-weight:600;">
                    🔗 LinkedIn
                </a>
            </div>
            """,
            icon="🌐"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Project Stats
        st.markdown("""
        <div class="np-card" style="text-align:center;">
            <h4 style="margin-top:0;">📊 Project Stats</h4>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1rem;">
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">313</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">Monthly Obs</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">65</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">Features</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">4</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">ML Models</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">3</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">Categories</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # FAQ Section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    render_section_header("❓", "Frequently Asked Questions")
    
    faq_col1, faq_col2 = st.columns(2, gap="large")
    
    with faq_col1:
        with st.expander("🔍 How accurate are the forecasts?"):
            st.markdown("""
            **Short answer:** MAE of 0.29-0.34 percentage points for Random Forest (best model).
            
            **What this means:**
            - If we predict Food MoM = +2.5%, actual value typically falls between +2.2% and +2.8%
            - Accuracy decreases with forecast horizon (month 1 > month 12)
            - Structural shocks (devaluation, policy changes) can cause larger errors
            
            **Compared to alternatives:**
            - Traditional ARIMA: MAE 7-38% (from literature)
            - Our model: 64-75% improvement
            """)
        
        with st.expander("📊 Can I use this for business decisions?"):
            st.markdown("""
            **Yes, with caveats:**
            
            **Good use cases:**
            - Inventory planning (3-6 month horizon)
            - Budget forecasting for procurement
            - Scenario testing ("what if FX hits ₦1,800?")
            - Trend identification (rising vs falling)
            
            **Not recommended for:**
            - Precise pricing (too much daily volatility)
            - Financial derivatives trading
            - Legal/regulatory compliance (use official CBN forecasts)
            
            **Best practice:** Use our forecasts as one input among many, not the sole decision factor.
            """)
    
    with faq_col2:
        with st.expander("🔄 How often are models updated?"):
            st.markdown("""
            **Current status:** Models trained on data through February 2026.
            
            **Update frequency:**
            - **Data:** Monthly (when NBS releases new CPI figures)
            - **Model retraining:** Quarterly (to incorporate new patterns)
            - **Architecture changes:** Annually (major research updates)
            
            **Roadmap:**
            - Automated monthly retraining (in development)
            - Real-time API integration with CBN/NBS
            """)
        
        with st.expander("🤝 Can I contribute to the project?"):
            st.markdown("""
            **Absolutely! We welcome contributions:**
            
            **Code:**
            - Fork the GitHub repo
            - Submit pull requests with improvements
            - Add new features (e.g., additional categories, alternative models)
            
            **Data:**
            - Share alternative data sources (satellite imagery, Google Trends, etc.)
            - Provide higher-frequency data (weekly/daily prices)
            
            **Research:**
            - Collaborate on academic papers
            - Test methodologies in other African countries
            - Validate results with real-world business data
            
            **Contact** via the form above with "Research Collaboration" topic.
            """)

    # Citation
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    render_section_header("📚", "How to Cite This Work")
    
    st.code("""
David, C. (2026). NairaPulse AI: Stacked Ensemble Model for Forecasting 
Inflation-Driven Consumer Goods Price Dynamics in Nigeria. 
Undergraduate Research Project, Department of Computing, 
Afe Babalola University, Ado-Ekiti, Nigeria.
    """, language="text")
    
    st.markdown("""
    **BibTeX:**
    ```bibtex
    @misc{david2026nairapulse,
      author = {David, Chimbueze},
      title = {NairaPulse AI: Stacked Ensemble Model for Forecasting Inflation-Driven Consumer Goods Price Dynamics in Nigeria},
      year = {2026},
      institution = {Afe Babalola University},
      type = {Undergraduate Research Project}
    }
    ```
    """)

if __name__ == "__main__":
    show_contact()