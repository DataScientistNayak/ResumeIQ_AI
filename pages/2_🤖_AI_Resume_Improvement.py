import streamlit as st

from components.sidebar import render_sidebar
from services.improve_resume import improve_resume
from services.section_detector import detect_sections
from utils.resume_loader import load_resume


st.set_page_config(
    page_title="AI Resume Improvement",
    page_icon="🤖",
    layout="wide",
)

render_sidebar()

st.title("🤖 AI Resume Improvement")

# ---------------------------------------
# Load Resume
# ---------------------------------------

_, resume_text = load_resume()

# ---------------------------------------
# Detect Resume Sections
# ---------------------------------------

sections = detect_sections(resume_text)

if not sections:
    st.warning("No resume sections detected.")
    st.stop()

selected_section = st.selectbox(
    "Select Resume Section",
    list(sections.keys()),
)

st.divider()

# ---------------------------------------
# Original Section
# ---------------------------------------

st.subheader("📄 Original Content")

st.text_area(
    label="Original",
    value=sections[selected_section],
    height=250,
    disabled=True,
)

st.divider()

# ---------------------------------------
# Improve Section
# ---------------------------------------

if st.button(
    "✨ Improve Section",
    type="primary",
    width="stretch",
):

    with st.spinner("Improving resume section using Gemini AI..."):

        try:

            improved = improve_resume(
                {
                    selected_section: sections[selected_section]
                }
            )

            improved_text = improved[selected_section]

        except Exception as e:

            st.error(f"AI Improvement failed.\n\n{e}")
            st.stop()

    st.success("Section improved successfully.")

    st.divider()

    # ---------------------------------------
    # Improved Content
    # ---------------------------------------

    st.subheader("🤖 AI Improved Content")

    st.text_area(
        label="Improved",
        value=improved_text,
        height=300,
    )

    st.download_button(
        label="⬇ Download Improved Section",
        data=improved_text,
        file_name=f"{selected_section}_improved.txt",
        mime="text/plain",
        width="stretch",
    )