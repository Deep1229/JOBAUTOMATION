
from collectors.job_collector import collect_jobs
from database.db import create_tables
from database.job_repository import save_jobs
from matching.scoring import score_job
from config_loader import load_profile
from matching.role_matching import match_role
from matching.filters import filter_job
from matching.location_matching import match_location
from matching.experience_matching import match_experience


create_tables()

profile = load_profile()

jobs = collect_jobs()
save_jobs(jobs)

print("Collected jobs:", len(jobs))
print("Jobs saved successfully.")

ranked_jobs = sorted(
    jobs,
    key=lambda job: score_job(job, profile),
    reverse=True
)
print("\nRanked job results:")



for job in ranked_jobs[:10]:
    print(
        "\nTitle:", job["title"],
        "| Company:", job["company"],
        "| Score:", score_job(job, profile),
        "| Experience match:", match_experience(job, profile)
    )
    