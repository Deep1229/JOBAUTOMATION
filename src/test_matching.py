from database.job_repository import get_all_jobs
from config_loader import load_profile
from matching.skills import match_skills


jobs = get_all_jobs()
profile = load_profile()

for job in jobs[:5]:
    job_data = {
        "title": job[1],
        "company": job[2],
        "location": job[3],
        "url": job[4],
        "source": job[5],
        "job_id": job[6],
        "description": job[8] if len(job) > 8 else ""
    }

    matched_skills = match_skills(job_data, profile)

    print("\nJob:", job_data["title"])
    print("Company:", job_data["company"])
    print("Matched skills:", matched_skills)