def normalize_job(job):
    return {
        "title": job.get("title"),
        "company": job.get("company"),
        "location": job.get("location", {}).get("name"),
        "url": job.get("absolute_url"),
        "source": "greenhouse",
        "job_id": job.get("id"),
    }