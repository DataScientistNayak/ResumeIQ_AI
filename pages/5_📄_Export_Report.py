import streamlit as st

from components.sidebar import render_sidebar

from services.csv_export import export_analysis_csv
from services.json_export import export_analysis_json
from services.pdf_export import generate_report

from utils.analysis_manager import get_analysis
from utils.resume_loader import load_resume


st.set_page_config(
    page_title="Export Report",
    page_icon="📄",
    layout="wide",
)

render_sidebar()

st.title("📄 Export Resume Analysis Report")

# ---------------------------------------
# Load Resume
# ---------------------------------------

_, resume_text = load_resume()

# ---------------------------------------
# Analyze Resume
# ---------------------------------------

try:

    analysis = get_analysis(resume_text)

except Exception as e:

    st.error(f"Analysis failed.\n\n{e}")
    st.stop()

st.success("Resume analyzed successfully.")

st.divider()

# ---------------------------------------
# Resume Overview
# ---------------------------------------

st.subheader("Resume Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "ATS Score",
        f"{analysis['ats']['overall_score']}/100",
    )

with col2:
    st.metric(
        "Skills Found",
        analysis["skills"]["count"],
    )

with col3:
    st.metric(
        "Word Count",
        analysis["resume"]["word_count"],
    )

st.divider()

# ---------------------------------------
# Export Buttons
# ---------------------------------------

st.subheader("Download Reports")

col1, col2, col3 = st.columns(3)

# PDF
with col1:

    try:

        pdf_data = generate_report(analysis)

        st.download_button(
            label="📄 PDF Report",
            data=pdf_data,
            file_name="ResumeIQ_Report.pdf",
            mime="application/pdf",
            width="stretch",
        )

    except Exception as e:

        st.error(f"PDF Export Failed\n\n{e}")

# JSON
with col2:

    try:

        json_data = export_analysis_json(analysis)

        st.download_button(
            label="🗂 JSON Report",
            data=json_data,
            file_name="ResumeIQ_Report.json",
            mime="application/json",
            width="stretch",
        )

    except Exception as e:

        st.error(f"JSON Export Failed\n\n{e}")

# CSV
with col3:

    try:

        csv_data = export_analysis_csv(analysis)

        st.download_button(
            label="📊 CSV Report",
            data=csv_data,
            file_name="ResumeIQ_Report.csv",
            mime="text/csv",
            width="stretch",
        )

    except Exception as e:

        st.error(f"CSV Export Failed\n\n{e}")

st.divider()

# ---------------------------------------
# Resume Statistics
# ---------------------------------------

st.subheader("Resume Statistics")

stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:

    st.metric(
        "Characters",
        analysis["resume"]["character_count"],
    )

with stats_col2:

    st.metric(
        "Lines",
        analysis["resume"]["line_count"],
    )

with stats_col3:

    st.metric(
        "Detected Sections",
        len(analysis["sections"]),
    )

st.divider()

# ---------------------------------------
# Skills
# ---------------------------------------

st.subheader("Detected Skills")

skills = analysis["skills"]["skills"]

if skills:

    cols = st.columns(4)

    for index, skill in enumerate(skills):
        cols[index % 4].success(skill)

else:

    st.warning("No technical skills detected.")

st.divider()

# ---------------------------------------
# ATS Suggestions
# ---------------------------------------

st.subheader("ATS Suggestions")

if analysis["ats"]["suggestions"]:

    for suggestion in analysis["ats"]["suggestions"]:
        st.write(f"• {suggestion}")

else:

    st.success("No ATS improvements suggested.")