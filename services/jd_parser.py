"""
Job Description Parser

Extracts structured information from a job description.
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional

from services.skill_extractor import extract_skills


EDUCATION_KEYWORDS = [
    "b.tech",
    "btech",
    "b.e",
    "be",
    "bachelor",
    "master",
    "m.tech",
    "mtech",
    "mca",
    "bca",
    "phd",
]

EXPERIENCE_PATTERNS = [
    r"(\d+)\+?\s+years",
    r"(\d+)\s*-\s*(\d+)\s+years",
    r"minimum\s+(\d+)\s+years",
]

RESPONSIBILITY_HEADINGS = [
    "responsibilities",
    "roles",
    "role",
    "what you'll do",
    "what you will do",
    "job responsibilities",
]


def extract_experience(text: str) -> Optional[str]:
    """
    Extract experience requirement.
    """

    text = text.lower()

    for pattern in EXPERIENCE_PATTERNS:

        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return None


def extract_education(text: str) -> List[str]:
    """
    Extract education requirements.
    """

    text = text.lower()

    found = {
        keyword
        for keyword in EDUCATION_KEYWORDS
        if keyword in text
    }

    return sorted(found)


def extract_responsibilities(text: str) -> List[str]:
    """
    Extract job responsibilities.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    responsibilities: List[str] = []

    capture = False

    for line in lines:

        lower = line.lower()

        if any(
            heading == lower.rstrip(":")
            for heading in RESPONSIBILITY_HEADINGS
        ):
            capture = True
            continue

        if not capture:
            continue

        if line.isupper() and len(line.split()) <= 5:
            break

        if re.match(r"^[-•]", line):

            responsibilities.append(
                re.sub(
                    r"^[-•]\s*",
                    "",
                    line,
                )
            )

        elif re.match(r"^\d+[\).\s]", line):

            responsibilities.append(line)

    return responsibilities


def parse_job_description(
    job_description: str,
) -> Dict:
    """
    Parse a Job Description into structured data.
    """

    job_description = job_description.strip()

    skills = extract_skills(job_description)

    return {
        "skills": skills["skills"],
        "skill_count": skills["count"],
        "experience": extract_experience(job_description),
        "education": extract_education(job_description),
        "responsibilities": extract_responsibilities(job_description),
        "raw_text": job_description,
    }