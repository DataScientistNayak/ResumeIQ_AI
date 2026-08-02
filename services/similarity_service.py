"""
Resume ↔ Job Description Similarity Service
"""

from __future__ import annotations

from typing import Dict, List

from sentence_transformers import util

from utils.cache import load_sentence_transformer


def load_model():
    """
    Load the cached SentenceTransformer model.
    """
    return load_sentence_transformer()


def semantic_similarity(
    text1: str,
    text2: str,
) -> float:
    """
    Calculate semantic similarity between two texts.

    Returns a percentage score (0-100).
    """

    if not text1.strip() or not text2.strip():
        return 0.0

    model = load_model()

    embeddings = model.encode(
        [text1, text2],
        convert_to_tensor=True,
        normalize_embeddings=True,
    )

    similarity = util.cos_sim(
        embeddings[0],
        embeddings[1],
    ).item()

    similarity = max(0.0, min(1.0, similarity))

    return round(similarity * 100, 2)


def skill_gap(
    resume_skills: List[str],
    jd_skills: List[str],
) -> Dict:
    """
    Compare resume skills against Job Description skills.
    """

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower()
        for skill in jd_skills
    }

    matched = sorted(
        resume_set & jd_set
    )

    missing = sorted(
        jd_set - resume_set
    )

    additional = sorted(
        resume_set - jd_set
    )

    match_percentage = (
        round(
            (len(matched) / len(jd_set)) * 100,
            2,
        )
        if jd_set
        else 0.0
    )

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "additional_skills": additional,
        "match_percentage": match_percentage,
    }


def compare_resume_with_jd(
    resume_text: str,
    resume_skills: List[str],
    jd_text: str,
    jd_skills: List[str],
) -> Dict:
    """
    Perform complete Resume vs Job Description analysis.
    """

    semantic_score = semantic_similarity(
        resume_text,
        jd_text,
    )

    gap = skill_gap(
        resume_skills,
        jd_skills,
    )

    overall_score = round(
        (
            semantic_score * 0.60
            + gap["match_percentage"] * 0.40
        ),
        2,
    )

    return {
        "overall_match": overall_score,
        "semantic_similarity": semantic_score,
        "skill_match": gap["match_percentage"],
        "matched_skills": gap["matched_skills"],
        "missing_skills": gap["missing_skills"],
        "additional_skills": gap["additional_skills"],
    }