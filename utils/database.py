import sqlite3

conn = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    prediction TEXT,
    confidence REAL,
    image_path TEXT
)
""")

conn.commit()


def save_prediction(
    username,
    prediction,
    confidence,
    image_path
):

    cursor.execute(
        """
        INSERT INTO history
        (
            username,
            prediction,
            confidence,
            image_path
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            username,
            prediction,
            confidence,
            image_path
        )
    )

    conn.commit()


def get_all_predictions():

    cursor.execute("""
    SELECT
        id,
        username,
        prediction,
        confidence,
        image_path
    FROM history
    ORDER BY id DESC
    """)

    return cursor.fetchall()


def get_user_predictions(username):

    cursor.execute(
        """
        SELECT
            id,
            username,
            prediction,
            confidence,
            image_path
        FROM history
        WHERE username = ?
        ORDER BY id DESC
        """,
        (username,)
    )

    return cursor.fetchall()


def delete_prediction(prediction_id):

    cursor.execute(
        """
        DELETE FROM history
        WHERE id = ?
        """,
        (prediction_id,)
    )

    conn.commit()


def get_total_users():

    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    """)

    total = cursor.fetchone()[0]

    return total


def get_total_predictions():

    cursor.execute("""
    SELECT COUNT(*)
    FROM history
    """)

    total = cursor.fetchone()[0]

    return total