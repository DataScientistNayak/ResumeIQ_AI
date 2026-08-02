"""
Analysis Session Manager
"""

from __future__ import annotations

from typing import Dict, Any

import streamlit as st

from services.resume_analyzer import analyze_resume


SESSION_KEY = "resume_analysis"


def get_analysis(
    resume_text: str,
) -> Dict[str, Any]:
    """
    Analyze the uploaded resume only once per session.

    Returns the cached analysis if it already exists.
    """

    if SESSION_KEY not in st.session_state:

        st.session_state[SESSION_KEY] = analyze_resume(
            resume_text
        )

    return st.session_state[SESSION_KEY]


def clear_analysis() -> None:
    """
    Remove cached resume analysis from the session.
    """

    st.session_state.pop(
        SESSION_KEY,
        None,
    )