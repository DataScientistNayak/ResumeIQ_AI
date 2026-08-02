"""
Skill Extraction Service

Uses spaCy and rule-based normalization to identify technical skills
from resumes. Designed for production use in ResumeIQ AI.
"""

from __future__ import annotations

import re
from typing import Dict, Set

from utils.cache import load_spacy_model


def load_spacy():
    """
    Load the cached spaCy model.
    """
    return load_spacy_model()


# --------------------------------------------------
# Master Skill Database
# --------------------------------------------------

MASTER_SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",
    "sqlite",
    "react",
    "angular",
    "vue",
    "node.js",
    "express",
    "django",
    "flask",
    "fastapi",
    "streamlit",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "scikit-learn",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "plotly",
    "langchain",
    "langgraph",
    "gemini",
    "openai",
    "docker",
    "kubernetes",
    "git",
    "github",
    "linux",
    "aws",
    "azure",
    "gcp",
    "firebase",
    "rest api",
    "graphql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "computer vision",
    "nlp",
    "data science",
    "data analytics",
    "power bi",
    "tableau",
    "excel",
}

# --------------------------------------------------
# Alias Mapping
# --------------------------------------------------

ALIASES = {
    "postgres": "postgresql",
    "postgre": "postgresql",
    "postgresql database": "postgresql",
    "js": "javascript",
    "ts": "typescript",
    "node": "node.js",
    "tf": "tensorflow",
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "cv": "computer vision",
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "genai": "artificial intelligence",
    "github actions": "github",
    "google cloud": "gcp",
    "amazon web services": "aws",
    "ms excel": "excel",
    "powerbi": "power bi",
    "pytorch lightning": "pytorch",
}

# --------------------------------------------------
# Text Cleaning
# --------------------------------------------------


def clean_text(text: str) -> str:
    """
    Normalize text before extraction.
    """

    text = text.lower()
    text = re.sub(r"[^\w\s\+\#\.-]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------------------
# Normalize Skill
# --------------------------------------------------


def normalize(skill: str) -> str:
    """
    Normalize skill aliases.
    """

    skill = skill.lower().strip()

    return ALIASES.get(skill, skill)


# --------------------------------------------------
# Rule-Based Extraction
# --------------------------------------------------


def extract_from_dictionary(text: str) -> Set[str]:
    """
    Dictionary-based skill extraction.
    """

    found = set()

    for skill in MASTER_SKILLS:

        if skill in text:
            found.add(skill)

    return found


# --------------------------------------------------
# spaCy Extraction
# --------------------------------------------------


def extract_with_spacy(text: str) -> Set[str]:
    """
    spaCy-based skill extraction.
    """

    nlp = load_spacy()

    doc = nlp(text)

    found = set()

    for token in doc:

        value = normalize(token.text)

        if value in MASTER_SKILLS:
            found.add(value)

    for chunk in doc.noun_chunks:

        value = normalize(chunk.text)

        if value in MASTER_SKILLS:
            found.add(value)

    return found


# --------------------------------------------------
# Main Function
# --------------------------------------------------


def extract_skills(text: str) -> Dict:
    """
    Extract normalized technical skills from resume text.
    """

    cleaned = clean_text(text)

    skills = set()

    skills.update(
        extract_from_dictionary(cleaned)
    )

    skills.update(
        extract_with_spacy(cleaned)
    )

    normalized = sorted(
        {
            normalize(skill)
            for skill in skills
        }
    )

    return {
        "skills": normalized,
        "count": len(normalized),
    }