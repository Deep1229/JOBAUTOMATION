from collectors.job_collector import collect_jobs


jobs = collect_jobs()

print("Total jobs:", len(jobs))

for job in jobs[:5]:
    #print(job["company"], "-", job["title"])
    print(job)