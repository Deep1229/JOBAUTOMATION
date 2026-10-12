
from matching.skills import match_skills
from matching.role_matching import match_role
from matching.filters import filter_job
from matching.location_matching import match_location
from matching.experience_matching import match_experience
SKILL_WEIGHTS = {
    "go": 5,
    "golang": 5,
    "aws": 5,
    "aws lambda": 5,
    "step functions": 4,
    "terraform": 4,
    "jenkins": 3,
    "rest apis": 3,
    "git": 2,
    "java": 2,
    "cloudwatch": 2,
    "mongodb": 1,
    "postman": 1,
    "insomnia": 1,
    "ci/cd": 2,
}


def score_job(job, profile):
    # Reject jobs with excluded keywords
    if not filter_job(job, profile):
        return 0

    # Reject jobs with incompatible recognized experience requirements
    if not match_experience(job, profile):
        return 0

    # Calculate weighted skill coverage
    matched_skills = match_skills(job, profile)

    all_skills = (
        profile["skills"]["primary"]
        + profile["skills"]["secondary"]
    )

    total_weight = sum(
        SKILL_WEIGHTS.get(skill.lower(), 1)
        for skill in all_skills
    )

    matched_weight = sum(
        SKILL_WEIGHTS.get(skill.lower(), 1)
        for skill in matched_skills
    )

    skill_score = (
        (matched_weight / total_weight) * 100
        if total_weight else 0
    )

    # Role and location relevance
    role_score = 100 if match_role(job, profile) else 0
    location_score = 100 if match_location(job, profile) else 0

    # Final weighted score
    final_score = (
        skill_score * 0.60
        + role_score * 0.20
        + location_score * 0.10
        + 10  # Experience-compatible bonus
    )

    return round(min(final_score, 100), 2)