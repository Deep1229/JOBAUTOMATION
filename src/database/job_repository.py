from database.db import save_job
from database.db import get_connection


def save_jobs(jobs):
    for job in jobs:
        save_job(job)




def get_all_jobs(): 
    connection = get_connection()

    cursor = connection.cursor()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            company,
            location,
            url,
            source,
            job_id,
            collected_at
        FROM jobs
        ORDER BY collected_at DESC
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows