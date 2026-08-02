"""
Resume Improvement Panel Component
"""

from __future__ import annotations

from typing import List

import streamlit as st


def render_improvement_panel(suggestions: List[str]) -> None:
    """
    Display ATS improvement suggestions.
    """

    st.subheader("💡 Resume Improvement Suggestions")

    if not suggestions:
        st.success("Your resume looks ATS-friendly. No major improvements detected.")
        return

    for index, suggestion in enumerate(suggestions, start=1):
        with st.container(border=True):
            st.markdown(f"**{index}. {suggestion}**")


def render_missing_sections(missing_sections: List[str]) -> None:
    """
    Display missing resume sections.
    """

    st.subheader("📋 Missing Sections")

    if not missing_sections:
        st.success("All important resume sections are present.")
        return

    for section in missing_sections:
        st.warning(section.title())


def render_keyword_summary(
    matched_keywords: List[str],
) -> None:
    """
    Display matched ATS keywords.
    """

    st.subheader("🎯 ATS Keywords")

    if not matched_keywords:
        st.error("No ATS keywords detected.")
        return

    cols = st.columns(4)

    for index, keyword in enumerate(sorted(matched_keywords)):
        cols[index % 4].success(keyword)