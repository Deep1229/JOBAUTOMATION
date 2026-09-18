from collectors.greenhouse import get_greenhouse_jobs


jobs = get_greenhouse_jobs("stripe")

print("Number of jobs:", len(jobs))
print("First job:", jobs[0]["title"])