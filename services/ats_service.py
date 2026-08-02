"""
ATS Scoring Service

Calculates an ATS compatibility score based on:
- Resume length
- Presence of important sections
- Skills
- Contact information
- Keyword richness
- Formatting heuristics

Author: ResumeIQ AI
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Dict, List


# -----------------------------
# Configuration
# -----------------------------

REQUIRED_SECTIONS = {
    "education": 10,
    "experience": 15,
    "skills": 15,
    "projects": 10,
    "certifications": 5,
    "summary": 5,
}

COMMON_TECH_KEYWORDS = {
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "html",
    "css",
    "react",
    "angular",
    "node",
    "flask",
    "django",
    "fastapi",
    "streamlit",
    "docker",
    "kubernetes",
    "git",
    "github",
    "aws",
    "azure",
    "gcp",
    "tensorflow",
    "keras",
    "pytorch",
    "machine learning",
    "deep learning",
    "data science",
    "nlp",
    "computer vision",
    "langchain",
    "langgraph",
    "gemini",
    "openai",
    "rest api",
}


# -----------------------------
# Utility Functions
# -----------------------------


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def detect_email(text: str) -> bool:
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.search(pattern, text) is not None


def detect_phone(text: str) -> bool:
    pattern = r"(\+?\d[\d\s\-]{8,}\d)"
    return re.search(pattern, text) is not None


def detect_links(text: str) -> bool:
    patterns = [
        r"linkedin\.com",
        r"github\.com",
        r"portfolio",
    ]

    return any(re.search(p, text.lower()) for p in patterns)


def detect_sections(text: str) -> Dict[str, bool]:
    lower = text.lower()

    mapping = {
        "education": [
            "education",
            "academic",
            "qualification",
        ],
        "experience": [
            "experience",
            "work experience",
            "employment",
            "internship",
        ],
        "skills": [
            "skills",
            "technical skills",
            "core skills",
        ],
        "projects": [
            "projects",
            "project",
        ],
        "certifications": [
            "certification",
            "certifications",
            "licenses",
        ],
        "summary": [
            "summary",
            "profile",
            "objective",
            "about",
        ],
    }

    result = {}

    for section, keywords in mapping.items():
        result[section] = any(keyword in lower for keyword in keywords)

    return result


def keyword_statistics(text: str):
    lower = clean_text(text)

    matched = []

    for keyword in COMMON_TECH_KEYWORDS:
        if keyword in lower:
            matched.append(keyword)

    frequency = Counter(matched)

    return {
        "matched_keywords": sorted(list(frequency.keys())),
        "count": len(frequency),
    }


# -----------------------------
# Main ATS Calculation
# -----------------------------


def calculate_ats_score(text: str) -> Dict:
    """
    Returns a dictionary containing:

    overall_score
    section_score
    keyword_score
    formatting_score
    suggestions
    """

    score = 0

    suggestions: List[str] = []

    sections = detect_sections(text)

    # -----------------------
    # Contact Information
    # -----------------------

    if detect_email(text):
        score += 5
    else:
        suggestions.append("Add a professional email address.")

    if detect_phone(text):
        score += 5
    else:
        suggestions.append("Include a contact phone number.")

    if detect_links(text):
        score += 5
    else:
        suggestions.append(
            "Add your LinkedIn or GitHub profile."
        )

    # -----------------------
    # Resume Length
    # -----------------------

    words = len(text.split())

    if 350 <= words <= 900:
        score += 15
    elif words < 350:
        score += 8
        suggestions.append(
            "Resume looks short. Add more accomplishments."
        )
    else:
        score += 10
        suggestions.append(
            "Resume may be too long. Keep it concise."
        )

    # -----------------------
    # Sections
    # -----------------------

    section_score = 0

    for section, points in REQUIRED_SECTIONS.items():
        if sections[section]:
            section_score += points
        else:
            suggestions.append(
                f"Missing section: {section.title()}"
            )

    score += section_score

    # -----------------------
    # Keywords
    # -----------------------

    keyword_data = keyword_statistics(text)

    keyword_count = keyword_data["count"]

    if keyword_count >= 20:
        keyword_score = 25
    elif keyword_count >= 15:
        keyword_score = 22
    elif keyword_count >= 10:
        keyword_score = 18
    elif keyword_count >= 5:
        keyword_score = 12
    else:
        keyword_score = 5
        suggestions.append(
            "Include more relevant technical keywords."
        )

    score += keyword_score

    # -----------------------
    # Formatting Heuristics
    # -----------------------

    formatting_score = 0

    if "\t" not in text:
        formatting_score += 5

    if len(re.findall(r"•|-", text)) > 5:
        formatting_score += 5
    else:
        suggestions.append(
            "Use bullet points for better readability."
        )

    score += formatting_score

    # -----------------------
    # Normalize
    # -----------------------

    score = min(score, 100)

    return {
        "overall_score": score,
        "section_score": section_score,
        "keyword_score": keyword_score,
        "formatting_score": formatting_score,
        "matched_keywords": keyword_data["matched_keywords"],
        "sections": sections,
        "suggestions": suggestions,
    }