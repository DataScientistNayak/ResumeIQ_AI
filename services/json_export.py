"""
JSON Export Service
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Dict


def _build_export_data(analysis: Dict) -> Dict:
    """
    Build the JSON export dictionary.
    """

    return {
        "generated_at": datetime.now().isoformat(),
        "resume_statistics": analysis["resume"],
        "ats": analysis["ats"],
        "skills": analysis["skills"],
        "sections": analysis["sections"],
        "missing_sections": analysis["missing_sections"],
        "section_statistics": analysis["section_statistics"],
    }


def export_analysis_json(
    analysis: Dict,
) -> str:
    """
    Export resume analysis as formatted JSON.
    """

    return json.dumps(
        _build_export_data(analysis),
        indent=4,
        ensure_ascii=False,
    )


def save_analysis_json(
    analysis: Dict,
    file_path: str,
) -> None:
    """
    Save analysis JSON to disk.
    """

    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            _build_export_data(analysis),
            file,
            indent=4,
            ensure_ascii=False,
        )