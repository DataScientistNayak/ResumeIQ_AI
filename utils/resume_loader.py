"""
Resume Loader Utility
"""

from __future__ import annotations

from typing import Tuple

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from components.uploader import upload_resume

from utils.docx_parser import extract_docx_text
from utils.pdf_parser import extract_pdf_text
from utils.session_manager import (
    get_resume,
    has_resume,
    save_resume,
)


def load_resume() -> Tuple[UploadedFile, str]:
    """
    Load and cache the uploaded resume.

    Returns
    -------
    tuple
        (uploaded_file, resume_text)
    """

    # ---------------------------------------
    # Already loaded in this session
    # ---------------------------------------

    if has_resume():

        return get_resume()

    # ---------------------------------------
    # Upload Resume
    # ---------------------------------------

    uploaded_file = upload_resume()

    if uploaded_file is None:

        st.info("📄 Upload a PDF or DOCX resume to continue.")
        st.stop()

    # ---------------------------------------
    # Extract Text
    # ---------------------------------------

    try:

        extension = uploaded_file.name.lower().split(".")[-1]

        if extension == "pdf":

            resume_text = extract_pdf_text(
                uploaded_file
            )

        elif extension == "docx":

            resume_text = extract_docx_text(
                uploaded_file
            )

        else:

            st.error(
                "Unsupported file format."
            )
            st.stop()

    except Exception as e:

        st.error(
            f"Failed to read the uploaded resume.\n\n{e}"
        )
        st.stop()

    # ---------------------------------------
    # Save Session
    # ---------------------------------------

    save_resume(
        uploaded_file,
        resume_text,
    )

    return uploaded_file, resume_text