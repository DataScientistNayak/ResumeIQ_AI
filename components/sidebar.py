"""
Reusable Sidebar Component
"""

from __future__ import annotations

import streamlit as st


APP_VERSION = "v1.0.0"


def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.image(
            "assets/logo.png",
            width="stretch",
        )

        st.title("ResumeIQ AI")

        st.caption(
            "AI Powered Resume Analyzer & ATS Optimizer"
        )

        st.divider()

        st.markdown("### 🚀 Features")

        st.success("📊 Resume Analysis")
        st.success("🤖 AI Resume Improvement")
        st.success("🎯 Resume vs Job Match")
        st.success("💬 Resume Chat")
        st.success("📜 Analysis History")
        st.success("📄 Export Reports")

        st.divider()

        st.markdown("### ⚙️ System")

        st.write(f"**Version:** {APP_VERSION}")
        st.write("**AI Model:** Gemini 2.5 Flash")
        st.write("**Database:** SQLite")
        st.write("**Framework:** Streamlit")

        st.divider()

        st.markdown(
            """
### 🛠 Tech Stack

- Streamlit
- Gemini AI
- spaCy
- Sentence Transformers
- Plotly
- SQLite
- PyMuPDF
- python-docx
"""
        )

        st.divider()

        st.caption("© 2026 ResumeIQ AI")