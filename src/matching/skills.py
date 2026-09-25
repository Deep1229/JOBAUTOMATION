def match_skills(job, profile):
    title = job.get("title", "")
    description = job.get("description", "")

    job_text = f"{title} {description}".lower()

    matched_skills = []

    for skill in profile["skills"]["primary"]:
        if skill.lower() in job_text:
            matched_skills.append(skill)

    for skill in profile["skills"]["secondary"]:
        if skill.lower() in job_text:
            matched_skills.append(skill)

    return matched_skills