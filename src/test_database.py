from database.job_repository import get_all_jobs


jobs = get_all_jobs()

print("Jobs in database:", len(jobs))

for job in jobs[:5]:
    print(job)