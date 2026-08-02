"""
Resume Analytics Dashboard
"""

from __future__ import annotations

import streamlit as st
import plotly.express as px


def render_dashboard(analysis: dict) -> None:
    """
    Render complete analytics dashboard.
    """

    st.header("📊 Resume Analytics")

    ats = analysis["ats"]["overall_score"]
    skills = analysis["skills"]["count"]
    words = analysis["resume"]["word_count"]
    sections = len(analysis["sections"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("ATS Score", f"{ats}/100")
    c2.metric("Skills", skills)
    c3.metric("Words", words)
    c4.metric("Sections", sections)

    st.divider()

    stats = analysis["section_statistics"]

    if stats:

        names = []
        values = []

        for section, data in stats.items():
            names.append(section.title())
            values.append(data["words"])

        fig = px.bar(
            x=names,
            y=values,
            labels={
                "x": "Resume Sections",
                "y": "Word Count",
            },
            title="Words per Resume Section",
            text=values,
        )

        fig.update_layout(height=450)

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.divider()

    st.subheader("Section Statistics")

    table = []

    for section, data in stats.items():
        table.append(
            {
                "Section": section.title(),
                "Words": data["words"],
                "Lines": data["lines"],
                "Characters": data["characters"],
            }
        )

    st.dataframe(
        table,
        use_container_width=True,
        hide_index=True,
    )