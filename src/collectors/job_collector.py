from src.config_loader import load_companies
from src.collectors.greenhouse import get_greenhouse_jobs
from src.job_normalizer import normalize_job
from src.database.job_repository import save_jobs


def collect_jobs():
    companies = load_companies()

    all_jobs = []

    for company in companies:
        if company["ats"] == "greenhouse":
            jobs = get_greenhouse_jobs(company["board_token"])

            for job in jobs:
                job["company"] = company["name"]

                normalized_job = normalize_job(job)

                all_jobs.append(normalized_job)

    return all_jobs


if __name__ == "__main__":
    from src.database.db import create_tables
    from src.database.job_repository import save_jobs

    create_tables()
    jobs = collect_jobs()
    save_jobs(jobs)

    print(f"Collected {len(jobs)} jobs")
    print("Jobs saved to the database.")

    for job in jobs:
        print(job)