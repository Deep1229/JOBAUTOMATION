
def match_location(job, profile):
    job_location = job.get("location") or ""
    job_location = job_location.lower()

    preferred_locations = profile.get("locations", {}).get(
        "preferred", []
    )

    for location in preferred_locations:
        if location.lower() in job_location:
            return True

    return False