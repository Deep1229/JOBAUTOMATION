
import re


def match_experience(job, profile):
    description = job.get("description") or ""
    title = job.get("title") or ""

    job_text = f"{title} {description}".lower()

    min_exp = profile["employment"]["minimum_experience"]
    max_exp = profile["employment"]["maximum_experience"]

    # Find phrases such as "2+ years of experience"
    pattern = r"(\d+)\+?\s*(?:to|-)\s*(\d+)\s+years"
    range_match = re.search(pattern, job_text)

    if range_match:
        required_min = int(range_match.group(1))
        required_max = int(range_match.group(2))

        return required_min <= max_exp and required_max >= min_exp

    # Find phrases such as "3+ years of experience"
    pattern = r"(\d+)\+\s*years"
    minimum_match = re.search(pattern, job_text)

    if minimum_match:
        required_years = int(minimum_match.group(1))
        return required_years <= max_exp

    # No recognized requirement: don't reject automatically
    return True