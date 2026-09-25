from collectors.job_collector import collect_jobs
from database.db import create_tables
from database.job_repository import save_jobs



create_tables()


jobs = collect_jobs()
save_jobs(jobs)




print("Collected jobs:", len(jobs))
print("Jobs saved successfully.")

#print("Total jobs:", len(jobs))

#for job in jobs[:5]:
    #print(job["company"], "-", job["title"])
 #   print(job)