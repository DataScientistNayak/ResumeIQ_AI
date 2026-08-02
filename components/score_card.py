"""
ATS Score Card Component
"""

from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st


def _score_color(score: int) -> str:
    """
    Return color based on ATS score.
    """

    if score >= 80:
        return "#16a34a"  # Green

    if score >= 60:
        return "#f59e0b"  # Orange

    return "#dc2626"  # Red


def render_score_card(score: int) -> None:
    """
    Render ATS score gauge and summary.
    """

    color = _score_color(score)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={
                "suffix": "/100",
                "font": {"size": 42},
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                },
                "bar": {
                    "color": color,
                    "thickness": 0.35,
                },
                "steps": [
                    {
                        "range": [0, 50],
                        "color": "#ffe5e5",
                    },
                    {
                        "range": [50, 75],
                        "color": "#fff5cc",
                    },
                    {
                        "range": [75, 100],
                        "color": "#e8f8ec",
                    },
                ],
            },
        )
    )

    fig.update_layout(
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20,
        ),
        height=320,
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    if score >= 80:
        st.success("Excellent ATS compatibility.")

    elif score >= 60:
        st.warning(
            "Good ATS compatibility, but there is room for improvement."
        )

    else:
        st.error(
            "Resume needs significant ATS optimization."
        )