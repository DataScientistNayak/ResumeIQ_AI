"""
Skill Distribution Chart Component
"""

from __future__ import annotations

from collections import Counter
from typing import List

import plotly.express as px
import streamlit as st


CATEGORY_MAP = {
    "Programming": [
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "typescript",
    ],
    "Web": [
        "html",
        "css",
        "react",
        "angular",
        "vue",
        "node.js",
        "express",
        "flask",
        "django",
        "fastapi",
        "streamlit",
    ],
    "Database": [
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "oracle",
        "sqlite",
    ],
    "AI / ML": [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "tensorflow",
        "keras",
        "pytorch",
        "opencv",
        "scikit-learn",
        "langchain",
        "langgraph",
        "gemini",
        "openai",
        "computer vision",
        "nlp",
    ],
    "Cloud / DevOps": [
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "gcp",
        "github",
        "git",
        "linux",
        "firebase",
    ],
    "Analytics": [
        "power bi",
        "tableau",
        "excel",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "plotly",
        "data science",
        "data analytics",
    ],
}


def categorize_skills(skills: List[str]) -> Counter:
    """
    Categorize detected skills into technology domains.
    """

    counter = Counter()

    for skill in skills:

        skill_lower = skill.lower()

        found = False

        for category, values in CATEGORY_MAP.items():

            if skill_lower in values:

                counter[category] += 1
                found = True
                break

        if not found:
            counter["Other"] += 1

    return counter


def render_skill_chart(skills: List[str]) -> None:
    """
    Display a pie chart and list of detected skills.
    """

    if not skills:
        st.info("No skills detected.")
        return

    categories = categorize_skills(skills)

    fig = px.pie(
        names=list(categories.keys()),
        values=list(categories.values()),
        title="Skill Distribution",
        hole=0.45,
    )

    fig.update_layout(
        height=420,
        legend_title="Categories",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    st.subheader("Detected Skills")

    cols = st.columns(3)

    for index, skill in enumerate(sorted(skills)):
        cols[index % 3].success(skill)