import streamlit as st

from components.sidebar import render_sidebar

from services.resume_chat import (
    ask_resume_ai,
    ats_feedback,
    improve_summary,
    recommend_skills,
    suggest_interview_questions,
    suggest_projects,
)

from utils.resume_loader import load_resume


st.set_page_config(
    page_title="Resume Chat",
    page_icon="💬",
    layout="wide",
)

render_sidebar()

st.title("💬 Resume Chat Assistant")

# ---------------------------------------
# Load Resume
# ---------------------------------------

uploaded_file, resume_text = load_resume()

st.success(f"Loaded: {uploaded_file.name}")

st.divider()

# ---------------------------------------
# Quick AI Actions
# ---------------------------------------

st.subheader("⚡ Quick AI Actions")

col1, col2, col3 = st.columns(3)

# ATS Feedback
with col1:

    if st.button(
        "📋 ATS Feedback",
        width="stretch",
    ):

        with st.spinner("Analyzing resume..."):

            try:

                response = ats_feedback(
                    resume_text
                )

                st.markdown(response)

            except Exception as e:

                st.error(str(e))

# Improve Summary
with col2:

    if st.button(
        "📝 Improve Summary",
        width="stretch",
    ):

        with st.spinner("Improving summary..."):

            try:

                response = improve_summary(
                    resume_text
                )

                st.markdown(response)

            except Exception as e:

                st.error(str(e))

# Recommend Skills
with col3:

    if st.button(
        "🚀 Recommend Skills",
        width="stretch",
    ):

        with st.spinner("Generating recommendations..."):

            try:

                response = recommend_skills(
                    resume_text
                )

                st.markdown(response)

            except Exception as e:

                st.error(str(e))

st.divider()

# ---------------------------------------
# More AI Actions
# ---------------------------------------

col4, col5 = st.columns(2)

# Interview Questions
with col4:

    if st.button(
        "🎯 Interview Questions",
        width="stretch",
    ):

        with st.spinner("Generating interview questions..."):

            try:

                response = suggest_interview_questions(
                    resume_text
                )

                st.markdown(response)

            except Exception as e:

                st.error(str(e))

# Project Suggestions
with col5:

    if st.button(
        "💼 Project Suggestions",
        width="stretch",
    ):

        with st.spinner("Generating project ideas..."):

            try:

                response = suggest_projects(
                    resume_text
                )

                st.markdown(response)

            except Exception as e:

                st.error(str(e))

st.divider()

# ---------------------------------------
# AI Chat
# ---------------------------------------

st.subheader("🤖 Ask Anything About Your Resume")

question = st.text_area(
    "Your Question",
    height=120,
    placeholder=(
        "Examples:\n"
        "- How can I improve my ATS score?\n"
        "- What skills are missing?\n"
        "- Is my resume suitable for a Data Scientist role?\n"
        "- Rewrite my experience section."
    ),
)

if st.button(
    "💬 Ask AI",
    type="primary",
    width="stretch",
):

    if not question.strip():

        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Thinking..."):

        try:

            answer = ask_resume_ai(
                resume_text,
                question,
            )

            st.divider()

            st.subheader("AI Response")

            st.markdown(answer)

        except Exception as e:

            st.error(str(e))