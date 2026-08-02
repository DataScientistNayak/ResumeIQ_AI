"""
Job Match Dashboard Component
"""

from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st


def render_match_dashboard(result: dict) -> None:
    """
    Display Resume vs Job Description analysis.
    """

    overall = result["overall_match"]
    semantic = result["semantic_similarity"]
    skill = result["skill_match"]

    st.subheader("🎯 Job Match Analysis")

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=overall,
            number={
                "suffix": "%",
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                },
                "bar": {
                    "thickness": 0.35,
                },
                "steps": [
                    {
                        "range": [0, 50],
                        "color": "#ffdddd",
                    },
                    {
                        "range": [50, 75],
                        "color": "#fff4cc",
                    },
                    {
                        "range": [75, 100],
                        "color": "#ddffdd",
                    },
                ],
            },
        )
    )

    fig.update_layout(
        height=320,
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Semantic Similarity",
            f"{semantic:.2f}%",
        )

    with col2:

        st.metric(
            "Skill Match",
            f"{skill:.2f}%",
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if result["matched_skills"]:

            for skill in result["matched_skills"]:
                st.success(skill)

        else:

            st.info("No matched skills.")

    with col2:

        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:

            for skill in result["missing_skills"]:
                st.error(skill)

        else:

            st.success("No missing skills.")

    st.divider()

    st.subheader("⭐ Additional Resume Skills")

    if result["additional_skills"]:

        cols = st.columns(3)

        for index, skill in enumerate(result["additional_skills"]):
            cols[index % 3].info(skill)

    else:

        st.info("No additional skills found.")