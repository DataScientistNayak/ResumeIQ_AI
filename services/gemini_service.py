"""
Gemini Service

Centralized Gemini service used throughout ResumeIQ AI.
"""

from __future__ import annotations

from utils.cache import load_gemini_model


MODEL_NAME = "gemini-2.5-flash"

_model = load_gemini_model()


def generate_response(
    prompt: str,
    temperature: float = 0.3,
) -> str:
    """
    Generate a response using Gemini.
    """

    try:

        response = _model.generate_content(
            prompt,
            generation_config={
                "temperature": temperature,
            },
        )

        if hasattr(response, "text") and response.text:
            return response.text.strip()

        return "No response generated."

    except Exception as e:
        raise RuntimeError(
            f"Gemini API Error: {e}"
        ) from e


def resume_summary(text: str) -> str:
    """
    Generate an AI summary for the uploaded resume.
    """

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume.

Return the response in Markdown.

Include the following sections:

# Professional Summary

# Strengths

# Weaknesses

# Technical Skills

# ATS Suggestions

Resume:

{text}
"""

    return generate_response(prompt)


def improve_text(
    instruction: str,
    content: str,
) -> str:
    """
    Generic helper used by AI modules.
    """

    prompt = f"""
{instruction}

Content:

{content}
"""

    return generate_response(prompt)


def ask_ai(
    system_prompt: str,
    user_prompt: str,
) -> str:
    """
    Generic chat helper.
    """

    prompt = f"""
{system_prompt}

User:

{user_prompt}
"""

    return generate_response(prompt)