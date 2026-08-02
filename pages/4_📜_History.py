import json

import streamlit as st

from database.history import (
    clear_history,
    delete_history,
    get_history,
)
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Resume Analysis History",
    page_icon="📜",
    layout="wide",
)
render_sidebar()

st.title("📜 Resume Analysis History")

history = get_history()

if not history:
    st.info("No resume analysis history found.")
    st.stop()

st.markdown(f"### Total Analyses : {len(history)}")

st.divider()

if st.button(
    "🗑️ Clear Entire History",
    type="primary",
):

    clear_history()

    st.success("History cleared successfully.")

    st.rerun()

st.divider()

for record in history:

    with st.expander(
        f"{record['file_name']} | ATS : {record['ats_score']}/100"
    ):

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "ATS Score",
            record["ats_score"],
        )

        col2.metric(
            "Skills",
            record["skills_count"],
        )

        col3.metric(
            "Words",
            record["word_count"],
        )

        st.caption(
            f"Analyzed on : {record['created_at']}"
        )

        analysis = json.loads(
            record["analysis_json"]
        )

        st.subheader("Detected Skills")

        if analysis["skills"]["skills"]:

            cols = st.columns(4)

            for index, skill in enumerate(
                analysis["skills"]["skills"]
            ):

                cols[index % 4].success(skill)

        st.subheader("ATS Suggestions")

        for suggestion in analysis["ats"]["suggestions"]:
            st.write(f"• {suggestion}")

        st.subheader("Missing Sections")

        if analysis["missing_sections"]:

            for section in analysis["missing_sections"]:
                st.warning(section.title())

        else:

            st.success(
                "No missing sections."
            )

        st.subheader("Resume Sections")

        for section, content in analysis[
            "sections"
        ].items():

            with st.expander(
                section.title()
            ):

                st.write(content)

        st.divider()

        if st.button(
            "Delete",
            key=f"delete_{record['id']}",
        ):

            delete_history(
                record["id"]
            )

            st.success(
                "Record deleted."
            )

            st.rerun()