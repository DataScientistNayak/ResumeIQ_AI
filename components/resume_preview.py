"""
Resume Preview Component
"""

from __future__ import annotations

import streamlit as st


def render_resume_preview(
    sections: dict,
    resume_stats: dict,
) -> None:
    """
    Display parsed resume in a structured format.
    """

    st.subheader("📄 Resume Preview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Words",
            resume_stats["word_count"],
        )

    with col2:
        st.metric(
            "Characters",
            resume_stats["character_count"],
        )

    with col3:
        st.metric(
            "Lines",
            resume_stats["line_count"],
        )

    st.divider()

    if not sections:
        st.warning("No resume sections detected.")
        return

    display_order = [
        "summary",
        "education",
        "experience",
        "projects",
        "skills",
        "certifications",
        "achievements",
        "languages",
        "interests",
    ]

    for section in display_order:

        if section not in sections:
            continue

        content = sections[section].strip()

        if not content:
            continue

        with st.expander(
            section.title(),
            expanded=(section == "summary"),
        ):
            st.write(content)