import sqlite3

DB_NAME = "applications.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id TEXT PRIMARY KEY,
        name TEXT,
        address TEXT,
        qualifications TEXT,
        course TEXT,
        start_year TEXT,
        start_month TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_application(app_id, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO applications (id, name, address, qualifications, course, start_year, start_month)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        app_id,
        data["name"],
        data["address"],
        data["qualifications"],
        data["course"],
        data["start_year"],
        data["start_month"]
    ))

    conn.commit()
    conn.close()
