"""
Section Detector Service

Detects resume sections and extracts their content.

Used by:
- ATS Scoring
- Resume Analyzer
- AI Resume Improvement
- Job Matching

Author: ResumeIQ AI
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional


# ----------------------------------------------------
# Section Heading Variations
# ----------------------------------------------------

SECTION_PATTERNS = {
    "summary": [
        "summary",
        "professional summary",
        "profile",
        "career objective",
        "objective",
        "about me",
    ],
    "education": [
        "education",
        "academic background",
        "qualifications",
        "academic qualifications",
    ],
    "experience": [
        "experience",
        "professional experience",
        "work experience",
        "employment history",
        "work history",
        "internships",
        "internship",
    ],
    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects",
    ],
    "skills": [
        "skills",
        "technical skills",
        "core competencies",
        "competencies",
        "technical expertise",
    ],
    "certifications": [
        "certifications",
        "certification",
        "licenses",
        "licenses & certifications",
    ],
    "achievements": [
        "achievements",
        "awards",
        "honors",
        "accomplishments",
    ],
    "languages": [
        "languages",
        "language proficiency",
    ],
    "interests": [
        "interests",
        "hobbies",
        "extracurricular activities",
    ],
}


# ----------------------------------------------------
# Normalize Text
# ----------------------------------------------------

def normalize(text: str) -> List[str]:
    """
    Remove empty lines and trim whitespace.
    """

    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


# ----------------------------------------------------
# Detect Heading
# ----------------------------------------------------

def get_section_name(line: str) -> Optional[str]:
    """
    Return the standardized section name if the
    line is recognized as a section heading.
    """

    lower = line.lower().strip()
    lower = re.sub(r"[:\-]+$", "", lower)

    for section, headings in SECTION_PATTERNS.items():

        if lower in headings:
            return section

    return None


# ----------------------------------------------------
# Main Detector
# ----------------------------------------------------

def detect_sections(text: str) -> Dict[str, str]:
    """
    Detect and extract resume sections.

    Returns a dictionary like:

    {
        "education": "...",
        "skills": "...",
        ...
    }
    """

    lines = normalize(text)

    sections: Dict[str, str] = {}

    current_section: Optional[str] = None

    buffer: List[str] = []

    for line in lines:

        heading = get_section_name(line)

        if heading:

            if current_section is not None:

                sections[current_section] = (
                    "\n".join(buffer).strip()
                )

            current_section = heading
            buffer = []

        elif current_section:

            buffer.append(line)

    if current_section:

        sections[current_section] = (
            "\n".join(buffer).strip()
        )

    return sections


# ----------------------------------------------------
# Section Presence
# ----------------------------------------------------

def section_exists(
    sections: Dict[str, str],
    name: str,
) -> bool:
    """
    Check whether a section exists.
    """

    return (
        name in sections
        and bool(sections[name].strip())
    )


# ----------------------------------------------------
# Missing Sections
# ----------------------------------------------------

def missing_sections(
    sections: Dict[str, str],
) -> List[str]:
    """
    Return missing important resume sections.
    """

    required = [
        "summary",
        "education",
        "experience",
        "skills",
        "projects",
    ]

    return [
        section
        for section in required
        if not section_exists(
            sections,
            section,
        )
    ]


# ----------------------------------------------------
# Statistics
# ----------------------------------------------------

def section_statistics(
    sections: Dict[str, str],
) -> Dict[str, Dict[str, int]]:
    """
    Return statistics for every detected section.
    """

    stats = {}

    for section, content in sections.items():

        stats[section] = {
            "characters": len(content),
            "words": len(content.split()),
            "lines": len(content.splitlines()),
        }

    return stats