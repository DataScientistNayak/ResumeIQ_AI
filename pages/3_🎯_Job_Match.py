import streamlit as st

from components.match_dashboard import render_match_dashboard
from components.sidebar import render_sidebar

from services.jd_parser import parse_job_description
from services.similarity_service import compare_resume_with_jd

from utils.analysis_manager import get_analysis
from utils.resume_loader import load_resume


st.set_page_config(
    page_title="Resume vs Job Match",
    page_icon="🎯",
    layout="wide",
)

render_sidebar()

st.title("🎯 Resume vs Job Description Match")

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

    st.error(f"Resume analysis failed.\n\n{e}")
    st.stop()

st.divider()

# ---------------------------------------
# Job Description
# ---------------------------------------

st.subheader("Paste Job Description")

job_description = st.text_area(
    label="Job Description",
    height=300,
    placeholder="Paste the complete Job Description here...",
)

if not job_description.strip():
    st.info("Paste a Job Description to compare your resume.")
    st.stop()

# ---------------------------------------
# Compare
# ---------------------------------------

if st.button(
    "🎯 Analyze Match",
    type="primary",
    width="stretch",
):

    with st.spinner("Comparing Resume with Job Description..."):

        try:

            jd = parse_job_description(job_description)

            result = compare_resume_with_jd(
                resume_text=resume_text,
                resume_skills=analysis["skills"]["skills"],
                jd_text=job_description,
                jd_skills=jd["skills"],
            )

        except Exception as e:

            st.error(f"Comparison failed.\n\n{e}")
            st.stop()

    st.success("Comparison completed successfully.")

    st.divider()

    # ---------------------------------------
    # Dashboard
    # ---------------------------------------

    render_match_dashboard(result)

    st.divider()

    # ---------------------------------------
    # Required Skills
    # ---------------------------------------

    st.subheader("📌 Required Skills")

    if jd["skills"]:

        cols = st.columns(4)

        for index, skill in enumerate(jd["skills"]):
            cols[index % 4].info(skill)

    else:

        st.warning("No skills detected.")

    st.divider()

    # ---------------------------------------
    # Experience
    # ---------------------------------------

    st.subheader("💼 Experience Requirement")

    if jd["experience"]:
        st.success(jd["experience"])
    else:
        st.info("No experience requirement detected.")

    st.divider()

    # ---------------------------------------
    # Education
    # ---------------------------------------

    st.subheader("🎓 Education Requirement")

    if jd["education"]:

        for item in jd["education"]:
            st.success(item.title())

    else:

        st.info("No education requirement detected.")

    st.divider()

    # ---------------------------------------
    # Responsibilities
    # ---------------------------------------

    st.subheader("📋 Job Responsibilities")

    if jd["responsibilities"]:

        for responsibility in jd["responsibilities"]:
            st.write(f"• {responsibility}")

    else:

        st.info("No responsibilities detected.")

    st.divider()

    # ---------------------------------------
    # Missing Skills
    # ---------------------------------------

    st.subheader("❌ Missing Skills")

    if result["missing_skills"]:

        cols = st.columns(4)

        for index, skill in enumerate(result["missing_skills"]):
            cols[index % 4].error(skill)

    else:

        st.success("No missing skills.")

    st.divider()

    # ---------------------------------------
    # Matching Skills
    # ---------------------------------------

    st.subheader("✅ Matching Skills")

    if result["matched_skills"]:

        cols = st.columns(4)

        for index, skill in enumerate(result["matched_skills"]):
            cols[index % 4].success(skill)

    else:

        st.warning("No matching skills found.")

    st.divider()

    # ---------------------------------------
    # Additional Skills
    # ---------------------------------------

    st.subheader("⭐ Additional Resume Skills")

    if result["additional_skills"]:

        cols = st.columns(4)

        for index, skill in enumerate(result["additional_skills"]):
            cols[index % 4].info(skill)

    else:

        st.info("No additional skills found.")