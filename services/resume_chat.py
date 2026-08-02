"""
Resume Chat Service
"""

from __future__ import annotations

from services.gemini_service import ask_ai


SYSTEM_PROMPT = """
You are ResumeIQ AI.

You are an expert:
- ATS Resume Reviewer
- Career Coach
- Technical Interviewer
- Hiring Manager

Rules:
- Use ONLY the information available in the resume.
- Never invent projects, skills, companies or experience.
- Be concise and professional.
- Format answers using Markdown whenever appropriate.
"""


def ask_resume_ai(
    resume_text: str,
    question: str,
) -> str:
    """
    Ask questions about a resume.
    """

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    user_prompt = f"""
Resume:

{resume_text}

Question:

{question}
"""

    return ask_ai(
        SYSTEM_PROMPT,
        user_prompt,
    )


def suggest_interview_questions(
    resume_text: str,
) -> str:
    """
    Generate interview questions based on the resume.
    """

    return ask_resume_ai(
        resume_text,
        """
Generate 10 technical interview questions based ONLY on this resume.

Include:
- Easy
- Medium
- Hard

Format as numbered Markdown.
""",
    )


def suggest_projects(
    resume_text: str,
) -> str:
    """
    Suggest portfolio projects.
    """

    return ask_resume_ai(
        resume_text,
        """
Suggest 5 portfolio projects that would significantly improve this resume.

Mention:
- Project Name
- Technologies
- Difficulty
- Why it adds value
""",
    )


def ats_feedback(
    resume_text: str,
) -> str:
    """
    Generate ATS improvement suggestions.
    """

    return ask_resume_ai(
        resume_text,
        """
Review this resume for ATS optimization.

Include:

# ATS Score Analysis

# Missing Keywords

# Weak Sections

# Strong Sections

# Recommendations
""",
    )


def improve_summary(
    resume_text: str,
) -> str:
    """
    Rewrite the professional summary.
    """

    return ask_resume_ai(
        resume_text,
        """
Rewrite ONLY the Professional Summary.

Rules:
- ATS optimized
- Professional
- Strong action words
- Do not invent information
- Maximum 120 words
""",
    )


def improve_experience(
    resume_text: str,
) -> str:
    """
    Improve work experience bullet points.
    """

    return ask_resume_ai(
        resume_text,
        """
Rewrite the work experience section.

Rules:
- Keep facts unchanged.
- Use STAR-style bullet points.
- Strong action verbs.
- ATS optimized.
""",
    )


def recommend_skills(
    resume_text: str,
) -> str:
    """
    Recommend additional technical skills.
    """

    return ask_resume_ai(
        resume_text,
        """
Recommend additional technical skills that would improve this resume.

Group them into:

- Programming
- Frameworks
- Databases
- Cloud
- AI/ML
- Tools
""",
    )