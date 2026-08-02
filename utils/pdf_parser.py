"""
PDF Parser Utility
"""

from __future__ import annotations

import fitz  # PyMuPDF


def extract_pdf_text(pdf_file) -> str:
    """
    Extract text from a PDF resume.
    """

    try:
        document = fitz.open(
            stream=pdf_file.read(),
            filetype="pdf",
        )

        pages = []

        for page in document:

            text = page.get_text().strip()

            if text:
                pages.append(text)

        document.close()

        return "\n".join(pages)

    except Exception as e:
        raise RuntimeError(
            f"Failed to extract text from PDF: {e}"
        )