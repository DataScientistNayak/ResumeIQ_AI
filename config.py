"""
Application Configuration
"""

from __future__ import annotations

import os

from dotenv import load_dotenv


# ---------------------------------------
# Load Environment Variables
# ---------------------------------------

load_dotenv()


# ---------------------------------------
# API Keys
# ---------------------------------------

GEMINI_API_KEY: str | None = os.getenv(
    "GEMINI_API_KEY"
)


# ---------------------------------------
# Directories
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
):
    os.makedirs(
        folder,
        exist_ok=True,
    )


# ---------------------------------------
# Startup Validation
# ---------------------------------------

if not GEMINI_API_KEY:
    print(
        "[WARNING] GEMINI_API_KEY not found. AI features will not work."
    )