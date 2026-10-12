
def match_role(job, profile):
    title = job.get("title", "").lower()

    target_roles = profile.get("target_roles", [])

    for role in target_roles:
        if role.lower() in title:
            return True

    return False