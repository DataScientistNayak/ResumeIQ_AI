"""
CSV Export Service
"""

from __future__ import annotations

import csv
from io import StringIO
from typing import Dict


def export_analysis_csv(analysis: Dict) -> str:
    """
    Export resume analysis as CSV.
    Returns CSV data as a string.
    """

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow(["ResumeIQ AI Report"])
    writer.writerow([])

    writer.writerow(["Resume Statistics"])
    writer.writerow(["Metric", "Value"])
    writer.writerow(["ATS Score", analysis["ats"]["overall_score"]])
    writer.writerow(["Word Count", analysis["resume"]["word_count"]])
    writer.writerow(["Character Count", analysis["resume"]["character_count"]])
    writer.writerow(["Line Count", analysis["resume"]["line_count"]])
    writer.writerow(["Skills Count", analysis["skills"]["count"]])

    writer.writerow([])

    writer.writerow(["Detected Skills"])

    for skill in analysis["skills"]["skills"]:
        writer.writerow([skill])

    writer.writerow([])

    writer.writerow(["Missing Sections"])

    if analysis["missing_sections"]:
        for section in analysis["missing_sections"]:
            writer.writerow([section])
    else:
        writer.writerow(["None"])

    writer.writerow([])

    writer.writerow(["ATS Suggestions"])

    for suggestion in analysis["ats"]["suggestions"]:
        writer.writerow([suggestion])

    writer.writerow([])

    writer.writerow(["Section Statistics"])
    writer.writerow(
        [
            "Section",
            "Words",
            "Lines",
            "Characters",
        ]
    )

    for section, stats in analysis["section_statistics"].items():
        writer.writerow(
            [
                section.title(),
                stats["words"],
                stats["lines"],
                stats["characters"],
            ]
        )

    return output.getvalue()


def save_analysis_csv(
    analysis: Dict,
    file_path: str,
) -> None:
    """
    Save analysis CSV to disk.
    """

    csv_data = export_analysis_csv(analysis)

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        file.write(csv_data)