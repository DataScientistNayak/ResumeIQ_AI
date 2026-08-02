"""
Database Initialization
"""

from __future__ import annotations

import sqlite3

from config import DATABASE_NAME


def init_db() -> None:
    """
    Create the application's database tables if they do not exist.
    """

    with sqlite3.connect(DATABASE_NAME) as conn:

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                ats_score INTEGER NOT NULL,
                skills_count INTEGER NOT NULL,
                word_count INTEGER NOT NULL,
                analysis_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )