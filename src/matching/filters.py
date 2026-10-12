
def filter_job(job, profile):
    title = job.get("title", "").lower()

    excluded_keywords = profile.get("exclude", [])

    for keyword in excluded_keywords:
        if keyword.lower() in title:
            return False

    return True