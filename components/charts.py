"""
Charts Component
"""

from __future__ import annotations

from typing import Dict

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def render_section_distribution(section_stats: Dict) -> None:
    """
    Doughnut chart showing section-wise word distribution.
    """

    if not section_stats:
        return

    labels = []
    values = []

    for section, stats in section_stats.items():
        labels.append(section.title())
        values.append(stats["words"])

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.45,
        title="Section Distribution",
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def render_resume_statistics(resume_stats: Dict) -> None:
    """
    Resume statistics.
    """

    labels = [
        "Words",
        "Characters",
        "Lines",
    ]

    values = [
        resume_stats["word_count"],
        resume_stats["character_count"],
        resume_stats["line_count"],
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            text=values,
            textposition="outside",
        )
    )

    fig.update_layout(
        title="Resume Statistics",
        height=420,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def render_skill_match_chart(result: Dict) -> None:
    """
    Resume vs JD comparison.
    """

    labels = [
        "Overall",
        "Semantic",
        "Skills",
    ]

    values = [
        result["overall_match"],
        result["semantic_similarity"],
        result["skill_match"],
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            text=[f"{v:.1f}%" for v in values],
            textposition="outside",
        )
    )

    fig.update_layout(
        title="Resume vs Job Description",
        yaxis=dict(range=[0, 100]),
        height=420,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def render_skill_category_chart(skills: Dict) -> None:
    """
    Horizontal bar chart for skill categories.
    """

    if not skills:
        return

    labels = list(skills.keys())
    values = list(skills.values())

    fig = px.bar(
        x=values,
        y=labels,
        orientation="h",
        text=values,
        title="Skill Categories",
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )