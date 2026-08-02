"""
History Database Service
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from typing import Any, Dict, List, Optional

from config import DATABASE_NAME


def get_connection() -> sqlite3.Connection:
    """
    Return a configured SQLite connection.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def save_analysis(
    file_name: str,
    analysis: Dict[str, Any],
) -> None:
    """
    Save a resume analysis.
    """

    with get_connection() as conn:

        conn.execute(
            """
            INSERT INTO analysis_history
            (
                file_name,
                ats_score,
                skills_count,
                word_count,
                analysis_json,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                file_name,
                analysis["ats"]["overall_score"],
                analysis["skills"]["count"],
                analysis["resume"]["word_count"],
                json.dumps(analysis),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )


def get_history() -> List[Dict[str, Any]]:
    """
    Return all saved analyses.
    """

    with get_connection() as conn:

        rows = conn.execute(
            """
            SELECT *
            FROM analysis_history
            ORDER BY id DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]


def get_analysis(
    history_id: int,
) -> Optional[Dict[str, Any]]:
    """
    Return a single analysis record.
    """

    with get_connection() as conn:

        row = conn.execute(
            """
            SELECT *
            FROM analysis_history
            WHERE id = ?
            """,
            (history_id,),
        ).fetchone()

    return dict(row) if row else None


def delete_history(
    history_id: int,
) -> None:
    """
    Delete one analysis.
    """

    with get_connection() as conn:

        conn.execute(
            """
            DELETE FROM analysis_history
            WHERE id = ?
            """,
            (history_id,),
        )


def clear_history() -> None:
    """
    Delete all analyses.
    """

    with get_connection() as conn:

        conn.execute(
            """
            DELETE FROM analysis_history
            """
        )


def history_count() -> int:
    """
    Return total number of analyses.
    """

    with get_connection() as conn:

        count = conn.execute(
            """
            SELECT COUNT(*)
            FROM analysis_history
            """
        ).fetchone()[0]

    return count


def latest_analysis() -> Optional[Dict[str, Any]]:
    """
    Return the most recent analysis.
    """

    with get_connection() as conn:

        row = conn.execute(
            """
            SELECT *
            FROM analysis_history
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()

    return dict(row) if row else None