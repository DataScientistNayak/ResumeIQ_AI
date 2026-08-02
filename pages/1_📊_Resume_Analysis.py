import streamlit as st

from database.history import save_analysis

from components.improvement_panel import (
    render_improvement_panel,
    render_keyword_summary,
    render_missing_sections,
)
from components.resume_preview import render_resume_preview
from components.score_card import render_score_card
from components.skill_chart import render_skill_chart

from utils.analysis_manager import get_analysis
from utils.resume_loader import load_resume


st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Resume Analysis")

# ---------------------------------------
# Load Resume
# ---------------------------------------

uploaded_file, resume_text = load_resume()

analysis = get_analysis(resume_text)

# ---------------------------------------
# Save History Once
# ---------------------------------------

if "last_saved_file" not in st.session_state:
    st.session_state.last_saved_file = None

if st.session_state.last_saved_file != uploaded_file.name:

    try:

        save_analysis(
            uploaded_file.name,
            analysis,
        )

        st.session_state.last_saved_file = uploaded_file.name

    except Exception:
        pass

# ---------------------------------------
# Overview
# ---------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "ATS Score",
    f"{analysis['ats']['overall_score']}/100",
)

col2.metric(
    "Skills",
    analysis["skills"]["count"],
)

col3.metric(
    "Words",
    analysis["resume"]["word_count"],
)

st.divider()

# ---------------------------------------
# Tabs
# ---------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 ATS",
        "🛠 Skills",
        "📄 Resume",
        "⚠ Suggestions",
    ]
)

# ---------------------------------------
# ATS
# ---------------------------------------

with tab1:

    render_score_card(
        analysis["ats"]["overall_score"]
    )

    st.divider()

    render_keyword_summary(
        analysis["ats"]["matched_keywords"]
    )

# ---------------------------------------
# Skills
# ---------------------------------------

with tab2:

    render_skill_chart(
        analysis["skills"]["skills"]
    )

    st.divider()

    render_missing_sections(
        analysis["missing_sections"]
    )

# ---------------------------------------
# Resume
# ---------------------------------------

with tab3:

    render_resume_preview(
        analysis["sections"],
        analysis["resume"],
    )

# ---------------------------------------
# Suggestions
# ---------------------------------------

with tab4:

    render_improvement_panel(
        analysis["ats"]["suggestions"]
    )