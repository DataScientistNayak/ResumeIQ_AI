"""
Resume Analyzer Service

Orchestrates all resume analysis services.

Returns a single structured dictionary that the Streamlit
application can directly consume.
"""

from __future__ import annotations

from typing import Any, Dict

from services.ats_service import calculate_ats_score
from services.section_detector import (
    detect_sections,
    missing_sections,
    section_statistics,
)
from services.skill_extractor import extract_skills


def analyze_resume(resume_text: str) -> Dict[str, Any]:
    """
    Analyze a resume and return all analysis results.

    Parameters
    ----------
    resume_text : str

    Returns
    -------
    Dict[str, Any]
    """

    resume_text = resume_text.strip()

    if not resume_text:
        raise ValueError("Resume text is empty.")

    # Section Detection
    sections = detect_sections(resume_text)

    # Skill Extraction
    skill_result = extract_skills(resume_text)

    # ATS Score
    ats_result = calculate_ats_score(resume_text)

    # Missing Sections
    missing = missing_sections(sections)

    # Section Statistics
    statistics = section_statistics(sections)

    # Resume Statistics
    total_words = len(resume_text.split())
    total_characters = len(resume_text)
    total_lines = len(
        [line for line in resume_text.splitlines() if line.strip()]
    )

    return {
        "resume": {
            "word_count": total_words,
            "character_count": total_characters,
            "line_count": total_lines,
        },
        "ats": ats_result,
        "skills": skill_result,
        "sections": sections,
        "missing_sections": missing,
        "section_statistics": statistics,
    }