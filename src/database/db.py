import sqlite3


DB_PATH = "data/jobs.db"


def get_connection():
    return sqlite3.connect(DB_PATH)




def create_tables():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            url TEXT,
            source TEXT NOT NULL,
            job_id INTEGER,
            description TEXT,
            collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(source, job_id)
        )
    """)

    connection.commit()
    connection.close()



def save_job(job):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO jobs (
            title,
            company,
            location,
            url,
            source,
            job_id,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        job["title"],
        job["company"],
        job["location"],
        job["url"],
        job["source"],
        job["job_id"],
        job["description"]
    ))

    connection.commit()
    connection.close()