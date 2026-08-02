"""
ResumeIQ AI
Main Dashboard
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from database.history import history_count
from database.init_db import init_db
from utils.analysis_manager import get_analysis
from utils.session_manager import (
    clear_resume,
    has_resume,
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

init_db()

# --------------------------------------------------
# Load Custom CSS
# --------------------------------------------------

css_path = Path("assets/style.css")

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# Header
# --------------------------------------------------

logo_path = Path("assets/logo.png")

if logo_path.exists():
    st.image(
        str(logo_path),
        width=180,
    )

st.title("📄 ResumeIQ AI")
st.caption("AI-Powered Resume Analyzer & ATS Optimizer")

st.divider()

# --------------------------------------------------
# Dashboard Statistics
# --------------------------------------------------

history = history_count()
resume_loaded = has_resume()

ats_score = "--"
skills = "--"

if resume_loaded:

    analysis = get_analysis(
        st.session_state["resume_text"]
    )

    ats_score = analysis["ats"]["overall_score"]
    skills = analysis["skills"]["count"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Resume Loaded",
        "✅ Yes" if resume_loaded else "❌ No",
    )

with col2:
    st.metric(
        "ATS Score",
        ats_score,
    )

with col3:
    st.metric(
        "History",
        history,
    )

st.divider()

# --------------------------------------------------
# Main Dashboard
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🚀 Project Features")

    st.markdown(
        """
- ✅ Resume Analysis
- ✅ ATS Score
- ✅ Skill Extraction
- ✅ AI Resume Improvement
- ✅ Resume Chat Assistant
- ✅ Resume vs Job Description Match
- ✅ Analysis History
- ✅ Export Reports
"""
    )

with right:

    st.subheader("📄 Current Session")

    if resume_loaded:

        uploaded_file = st.session_state.get(
            "uploaded_file"
        )

        st.success(
            f"Loaded Resume: **{uploaded_file.name}**"
        )

        st.metric(
            "Detected Skills",
            skills,
        )

        if st.button(
            "🗑 Remove Resume",
            use_container_width=True,
        ):

            clear_resume()
            st.rerun()

    else:

        st.info(
            "Upload a resume from the **Resume Analysis** page to begin."
        )

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.info(
    "👈 Use the navigation menu on the left to access all ResumeIQ AI modules."
)