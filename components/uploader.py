"""
Resume Upload Component
"""

from __future__ import annotations

import streamlit as st


def upload_resume():
    """
    Display a reusable resume uploader.

    Returns
    -------
    UploadedFile | None
        The uploaded PDF/DOCX file.
    """

    return st.file_uploader(
        label="📄 Upload Your Resume",
        type=["pdf", "docx"],
        help="Supported formats: PDF (.pdf) and Microsoft Word (.docx)",
        accept_multiple_files=False,
    )