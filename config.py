"""
Application Configuration

Loads environment variables for both:
- Local Development (.env)
- Streamlit Community Cloud (Secrets)

Author: ResumeIQ AI
"""

from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv

# ---------------------------------------
# Load Local Environment Variables
# ---------------------------------------

load_dotenv()

# ---------------------------------------
# Gemini API Key
# ---------------------------------------

# Default to .env (local development)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Override with Streamlit Secrets if available
try:
    if "GEMINI_API_KEY" in st.secrets:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    # Running outside Streamlit or no secrets configured
    pass

# ---------------------------------------
# Application Directories
# ---------------------------------------

UPLOAD_FOLDER = "uploads"
GENERATED_FOLDER = "generated"

DATABASE_NAME = "database/resumeiq.db"

# ---------------------------------------
# Create Required Directories
# ---------------------------------------

for folder in (
    UPLOAD_FOLDER,
    GENERATED_FOLDER,
    os.path.dirname(DATABASE_NAME),
):
    if folder:
        os.makedirs(
            folder,
            exist_ok=True,
        )

# ---------------------------------------
# Startup Validation
# ---------------------------------------

if not GEMINI_API_KEY:
    print(
        "[WARNING] GEMINI_API_KEY not found.\n"
        "AI-powered features will be disabled until a valid API key is provided."
    )