import sqlite3
from datetime import datetime


class HistoryService:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/agrimind.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            city TEXT,

            crop TEXT,

            confidence REAL
        )
        """)

        self.conn.commit()

    def save_prediction(
        self,
        city,
        crop,
        confidence
    ):

        self.cursor.execute(
            """
            INSERT INTO predictions
            (date,city,crop,confidence)

            VALUES(?,?,?,?)
            """,
            (
                datetime.now().strftime("%d-%m-%Y %H:%M"),
                city,
                crop,
                confidence
            )
        )

        self.conn.commit()

    def get_history(self):

        self.cursor.execute(
            """
            SELECT
            date,
            city,
            crop,
            confidence

            FROM predictions

            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()