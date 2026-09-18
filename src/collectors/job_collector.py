from config_loader import load_companies
from collectors.greenhouse import get_greenhouse_jobs
from job_normalizer import normalize_job


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