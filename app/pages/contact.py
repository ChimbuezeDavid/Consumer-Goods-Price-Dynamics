# app/pages/contact.py
"""
NairaPulse AI - Contact & Collaboration Page
Functional contact form via FormSubmit.co. IcoFont icons. No emojis.
"""

import re
import streamlit as st
import streamlit.components.v1 as components
from app.ui_components import render_hero, render_section_header

# ---------------------------------------------------------------------------
# CONTACT EMAIL - submissions are delivered here via FormSubmit.co
# ---------------------------------------------------------------------------
CONTACT_EMAIL = "developercdo@gmail.com"

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _is_valid_email(address: str) -> bool:
    return bool(_EMAIL_RE.match(address.strip()))


def show_contact():
    """Render the Contact & Collaboration page."""
    render_hero(
        title="Contact & Collaboration",
        subtitle="We welcome questions, research inquiries, academic partnerships, and constructive feedback from practitioners and researchers worldwide."
    )

    col1, col2 = st.columns([1.65, 1], gap="large")

    # -----------------------------------------------------------------------
    # LEFT COLUMN - Contact Form
    # -----------------------------------------------------------------------
    with col1:
        render_section_header(
            '<i class="icofont-email np-icon-primary"></i>',
            "Send a Message"
        )

        st.markdown("""
        Whether you have a question about the forecasting methodology, spotted an issue, 
        or are interested in academic collaboration or data exchange, use the form below. 
        Submissions are delivered directly to the research team.
        """)

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input(
                "Full Name *",
                placeholder="e.g. Adaeze Okonkwo or James Robertson",
                help="Your full name"
            )

            email = st.text_input(
                "Email Address *",
                placeholder="you@example.com",
                help="We will reply to this address within 24 to 48 hours"
            )

            topic = st.selectbox(
                "Topic *",
                [
                    "General Inquiry",
                    "Research Collaboration",
                    "Academic Partnership",
                    "Technical Feedback",
                    "Bug Report",
                    "Feature Suggestion",
                    "Data Request / Sharing",
                    "Media / Press Inquiry",
                ],
                help="Select the category that best describes your message"
            )

            message = st.text_area(
                "Your Message *",
                height=200,
                placeholder="Describe your inquiry in as much detail as you wish...",
                help="Please be as specific as possible; it helps us respond more usefully."
            )

            priority = st.radio(
                "Priority",
                ["Standard", "High", "Urgent"],
                horizontal=True,
                help="Mark as High or Urgent only for time-sensitive matters"
            )

            newsletter = st.checkbox(
                "Notify me of major model updates and new research outputs (max 2 emails/month)",
            )

            submitted = st.form_submit_button(
                "SEND MESSAGE",
                use_container_width=True,
                type="primary"
            )

            if submitted:
                # --- Client-side validation ---
                errors = []
                if not name.strip():
                    errors.append("Full name is required.")
                if not email.strip():
                    errors.append("Email address is required.")
                elif not _is_valid_email(email):
                    errors.append("Please enter a valid email address (e.g. you@example.com).")
                if not message.strip():
                    errors.append("Message body cannot be empty.")

                if errors:
                    for err in errors:
                        st.error(f"  {err}")
                else:
                    # -------------------------------------------------------
                    # FORM DELIVERY - FormSubmit.co (no credentials required)
                    # Injects a hidden HTML form and submits it programmatically
                    # to deliver the message to CONTACT_EMAIL.
                    # -------------------------------------------------------
                    newsletter_str = "Yes - add to mailing list" if newsletter else "No"
                    form_html = f"""
                    <form id="nairapulse-contact"
                          action="https://formsubmit.co/{CONTACT_EMAIL}"
                          method="POST"
                          style="display:none;">
                        <input type="hidden" name="_captcha"     value="false">
                        <input type="hidden" name="_template"    value="table">
                        <input type="hidden" name="_subject"     value="NairaPulse AI - Contact Form: {topic} ({priority})">
                        <input type="hidden" name="Name"         value="{name}">
                        <input type="hidden" name="Email"        value="{email}">
                        <input type="hidden" name="Topic"        value="{topic}">
                        <input type="hidden" name="Priority"     value="{priority}">
                        <input type="hidden" name="Newsletter"   value="{newsletter_str}">
                        <input type="hidden" name="Message"      value="{message.replace(chr(10), ' | ')}">
                    </form>
                    <script>
                        document.getElementById("nairapulse-contact").submit();
                    </script>
                    """
                    components.html(form_html, height=0)

                    st.success(
                        f"**Message received, {name.split()[0]}!** "
                        f"Your {topic.lower()} has been forwarded to the research team. "
                        f"We will reply to **{email}** within 24 to 48 hours."
                    )

                    if newsletter:
                        st.info(
                            "You have been added to the NairaPulse AI update list. "
                            "Expect no more than two notifications per month."
                        )

        # -------------------------------------------------------------------
        # Alternative Contact Methods
        # -------------------------------------------------------------------
        st.markdown("<br>", unsafe_allow_html=True)
        render_section_header(
            '<i class="icofont-phone-circle np-icon-primary"></i>',
            "Other Ways to Reach Us"
        )

        alt_col1, alt_col2 = st.columns(2, gap="medium")

        with alt_col1:
            st.markdown("""
            <div class="np-card">
                <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.8rem;">
                    <i class="icofont-email np-icon-primary np-icon-md"></i>
                    <strong>Personal Email</strong>
                </div>
                <div style="color:var(--np-muted); font-size:0.95rem; line-height:1.7;">
                    developercdo@gmail.com<br>
                    <em style="font-size:0.85rem;">For direct correspondence and academic inquiries</em>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with alt_col2:
            st.markdown("""
            <div class="np-card">
                <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.8rem;">
                    <i class="icofont-brand-github np-icon-primary np-icon-md"></i>
                    <strong>GitHub Issues</strong>
                </div>
                <div style="color:var(--np-muted); font-size:0.95rem; line-height:1.7;">
                    Found a bug or want to request a feature?<br>
                    Open a detailed issue on the project repository.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # RIGHT COLUMN - Developer & Project Info
    # -----------------------------------------------------------------------
    with col2:
        render_section_header(
            '<i class="icofont-user np-icon-primary"></i>',
            "About the Developer"
        )

        st.markdown(f"""
        <div class="np-card" style="background:linear-gradient(135deg, var(--np-primary), var(--np-accent)); color:white;">
            <h4 style="color:white; margin-top:0; font-size:1rem; letter-spacing:0.05em; opacity:0.8;">
                RESEARCH LEAD
            </h4>
            <div style="font-size:1.6rem; font-weight:800; margin:0.5rem 0;">Chimbueze David</div>
            <div style="margin:1rem 0; line-height:1.9; font-size:0.95rem;">
                <strong>Institution:</strong> Afe Babalola University (ABUAD)<br>
                <strong>Department:</strong> Computing<br>
                <strong>Programme:</strong> B.Sc. Computer Science<br>
                <strong>Year:</strong> Final Year, 2025/2026<br>
                <strong>Project Type:</strong> Undergraduate Research
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("""
        <div class="np-card">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:1rem;">
                <i class="icofont-link np-icon-primary np-icon-md"></i>
                <strong style="color:var(--np-primary);">Online Profiles</strong>
            </div>
            <div style="line-height:2.4;">
                <a href="https://github.com/ChimbuezeDavid" target="_blank"
                   style="color:var(--np-primary); text-decoration:none; font-weight:600;
                          display:flex; align-items:center; gap:0.4rem;">
                    <i class="icofont-brand-github"></i> GitHub: ChimbuezeDavid
                </a>
                <a href="https://x.com/ChimezeDavid" target="_blank"
                   style="color:var(--np-primary); text-decoration:none; font-weight:600;
                          display:flex; align-items:center; gap:0.4rem;">
                    <i class="icofont-twitter"></i> X (Twitter): @ChimezeDavid
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Project Stats
        st.markdown("""
        <div class="np-card" style="text-align:center;">
            <div style="display:flex; align-items:center; gap:0.5rem; justify-content:center; margin-bottom:1rem;">
                <i class="icofont-pie-chart np-icon-primary np-icon-md"></i>
                <strong style="color:var(--np-primary);">Project Snapshot</strong>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:0.5rem;">
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">313</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">Monthly Observations</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">65</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">Engineered Features</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">4</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">ML Models</div>
                </div>
                <div>
                    <div style="font-size:1.8rem; font-weight:800; color:var(--np-primary);">3</div>
                    <div style="color:var(--np-muted); font-size:0.85rem;">Price Categories</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # FAQ Section
    # -----------------------------------------------------------------------
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    render_section_header(
        '<i class="icofont-question-circle np-icon-primary"></i>',
        "Frequently Asked Questions"
    )

    faq_col1, faq_col2 = st.columns(2, gap="large")

    with faq_col1:
        with st.expander("How accurate are the forecasts?"):
            st.markdown("""
            The ensemble model achieves a Mean Absolute Error (MAE) of approximately 
            **0.26 to 0.31 percentage points** on the held-out test set, depending on category. 
            In practical terms, if the system forecasts a +2.5% month-over-month change 
            in food prices, the actual outturn typically falls between +2.2% and +2.8%.

            **Benchmark comparison:**  
            Traditional univariate ARIMA models applied to Nigerian CPI data produce MAEs 
            of 0.9 to 1.6 percentage points in the same evaluation window. The stacked 
            ensemble achieves a **64 to 75% reduction** relative to this baseline.

            **Limitations to note:**  
            Accuracy degrades at longer horizons (months 10 to 24), and unexpected structural 
            shocks such as sudden currency devaluations, subsidy removals, or external 
            commodity crises can produce forecast errors larger than the typical range.
            """)

        with st.expander("Can this be used to inform real business or policy decisions?"):
            st.markdown("""
            The system is designed to support, not replace, professional judgment. 
            It is well-suited for:

            - **Procurement and inventory planning** over a 3 to 6 month horizon
            - **Budget scenario analysis** for organisations with Nigeria-facing supply chains
            - **Policy research** and academic literature on emerging-market inflation dynamics
            - **Trend identification**: distinguishing rising from falling price regimes

            It is **not** recommended as a sole input for:
            - Financial derivatives pricing or trading
            - Legal or regulatory compliance reporting (use official CBN/NBS publications)
            - Precise day-to-day pricing decisions

            Best practice: treat NairaPulse AI forecasts as one quantitative input within a 
            broader analytical framework that also incorporates expert judgment and current events.
            """)

    with faq_col2:
        with st.expander("How frequently are models retrained?"):
            st.markdown("""
            **Current data vintage:** Models were trained on data through February 2026.

            **Update roadmap:**
            - **Data refresh:** Monthly, as the National Bureau of Statistics (NBS) 
              publishes updated CPI figures.
            - **Model retraining:** Quarterly, to incorporate new data patterns and 
              test whether the feature set requires adjustment.
            - **Architecture review:** Annually, or following major structural economic 
              events that may warrant a full modelling revision.

            An automated monthly retraining pipeline and API integration with NBS/CBN 
            data endpoints are on the development roadmap.
            """)

        with st.expander("How can I contribute to the project?"):
            st.markdown("""
            Contributions from the global research community are welcome in several forms:

            **Code contributions:**  
            Fork the GitHub repository, implement improvements or additional features, 
            and submit a pull request with a clear description of your changes.

            **Data contributions:**  
            Share alternative or complementary data sources such as satellite-derived 
            agricultural indices, high-frequency retail price surveys, Google Trends 
            proxies, or cross-border trade data that may improve forecast accuracy.

            **Research collaboration:**  
            We are interested in extending the methodology to other African countries, 
            validating results against business micro-data, and co-authoring applied 
            econometrics papers. Contact us via the form above with topic 
            **"Research Collaboration"**.

            **Feedback:**  
            Even a short note identifying a methodological concern, a data inconsistency, 
            or a usability issue is a valuable contribution.
            """)

    # -----------------------------------------------------------------------
    # Citation
    # -----------------------------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    render_section_header(
        '<i class="icofont-library np-icon-primary"></i>',
        "How to Cite This Work"
    )

    st.markdown("**APA 7th Edition:**")
    st.code("""
David, C. (2026). Development of a stacked ensemble model for forecasting price
dynamics of consumer goods in Nigeria.
Undergraduate Research Project, Department of Computing,
Afe Babalola University, Ado-Ekiti, Nigeria.
    """, language="text")

    st.markdown("**BibTeX:**")
    st.code("""
@misc{david2026stackedensemble,
  author      = {David, Chimbueze},
  title       = {Development of a Stacked Ensemble Model for Forecasting Price
                 Dynamics of Consumer Goods in {Nigeria}},
  year        = {2026},
  institution = {Afe Babalola University},
  type        = {Undergraduate Research Project},
  department  = {Department of Computing},
  address     = {Ado-Ekiti, Nigeria}
}
    """, language="bibtex")


if __name__ == "__main__":
    show_contact()