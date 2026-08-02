"""
PDF Export Service
"""

from __future__ import annotations

from io import BytesIO
from typing import Dict

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def generate_report(analysis: Dict) -> bytes:
    """
    Generate a PDF report from resume analysis.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "ResumeIQ AI Report",
            styles["Title"],
        )
    )

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # ATS Score
    # --------------------------------------------------

    ats = analysis["ats"]["overall_score"]

    elements.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats}/100",
            styles["Heading2"],
        )
    )

    elements.append(Spacer(1, 10))

    # --------------------------------------------------
    # Statistics Table
    # --------------------------------------------------

    table_data = [
        ["Metric", "Value"],
        ["Word Count", analysis["resume"]["word_count"]],
        ["Character Count", analysis["resume"]["character_count"]],
        ["Line Count", analysis["resume"]["line_count"]],
        ["Skills", analysis["skills"]["count"]],
        ["Detected Sections", len(analysis["sections"])],
    ]

    table = Table(table_data)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ]
        )
    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # ATS Suggestions
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "ATS Suggestions",
            styles["Heading2"],
        )
    )

    suggestions = analysis["ats"]["suggestions"]

    if suggestions:

        for suggestion in suggestions:
            elements.append(
                Paragraph(
                    f"• {suggestion}",
                    styles["BodyText"],
                )
            )

    else:

        elements.append(
            Paragraph(
                "No ATS improvements suggested.",
                styles["BodyText"],
            )
        )

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # Skills
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"],
        )
    )

    skills = analysis["skills"]["skills"]

    elements.append(
        Paragraph(
            ", ".join(skills) if skills else "No skills detected.",
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # Resume Sections
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "Resume Sections",
            styles["Heading2"],
        )
    )

    if analysis["sections"]:

        for section, content in analysis["sections"].items():

            elements.append(
                Paragraph(
                    section.title(),
                    styles["Heading3"],
                )
            )

            elements.append(
                Paragraph(
                    content.replace("\n", "<br/>"),
                    styles["BodyText"],
                )
            )

            elements.append(
                Spacer(1, 12)
            )

    else:

        elements.append(
            Paragraph(
                "No sections detected.",
                styles["BodyText"],
            )
        )

    # --------------------------------------------------
    # Build PDF
    # --------------------------------------------------

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf