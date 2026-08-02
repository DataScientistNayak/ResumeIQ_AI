"""
AI Resume Improvement Service
"""

from __future__ import annotations

from typing import Dict

from services.gemini_service import improve_text


SYSTEM_PROMPT = """
You are an expert ATS Resume Writer.

Improve ONLY the given resume section.

Rules:
- Keep the original meaning.
- Do NOT invent information.
- Improve grammar.
- Use strong action verbs.
- Make it ATS-friendly.
- Keep formatting clean.
- Return ONLY the improved section.
"""


def improve_section(
    section_name: str,
    section_text: str,
) -> str:
    """
    Improve a single resume section.
    """

    if not section_text.strip():
        return ""

    instruction = f"""
{SYSTEM_PROMPT}

Section Name:
{section_name}
"""

    return improve_text(
        instruction=instruction,
        content=section_text,
    )


def improve_resume(
    sections: Dict[str, str],
) -> Dict[str, str]:
    """
    Improve every detected resume section.
    """

    improved_sections = {}

    for section, content in sections.items():

        if not content.strip():
            improved_sections[section] = ""
            continue

        try:
            improved_sections[section] = improve_section(
                section,
                content,
            )

        except Exception:
            improved_sections[section] = content

    return improved_sections