"""
Session Manager

Stores and retrieves the uploaded resume.
"""

from __future__ import annotations

from typing import Optional, Tuple

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


UPLOADED_FILE_KEY = "uploaded_file"
RESUME_TEXT_KEY = "resume_text"
ANALYSIS_KEY = "resume_analysis"


def save_resume(
    uploaded_file: UploadedFile,
    resume_text: str,
) -> None:
    """
    Save the uploaded resume into the current session.
    """

    st.session_state[UPLOADED_FILE_KEY] = uploaded_file
    st.session_state[RESUME_TEXT_KEY] = resume_text


def get_resume() -> Tuple[
    Optional[UploadedFile],
    Optional[str],
]:
    """
    Retrieve the stored resume from the session.
    """

    return (
        st.session_state.get(UPLOADED_FILE_KEY),
        st.session_state.get(RESUME_TEXT_KEY),
    )


def has_resume() -> bool:
    """
    Check whether a resume has been uploaded.
    """

    return (
        RESUME_TEXT_KEY in st.session_state
        and st.session_state[RESUME_TEXT_KEY] is not None
    )


def clear_resume() -> None:
    """
    Remove the uploaded resume and cached analysis.
    """

    st.session_state.pop(
        UPLOADED_FILE_KEY,
        None,
    )

    st.session_state.pop(
        RESUME_TEXT_KEY,
        None,
    )

    st.session_state.pop(
        ANALYSIS_KEY,
        None,
    )