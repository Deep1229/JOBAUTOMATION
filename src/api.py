
from fastapi import FastAPI, Query, HTTPException

from database.job_repository import get_all_jobs
from config_loader import load_profile
from matching.scoring import score_job
from pydantic import BaseModel
from typing import Optional




class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: Optional[str] = None
    url: Optional[str] = None
    source: str
    job_id: Optional[int] = None
    collected_at: Optional[str] = None


class RankedJobResponse(JobResponse):
    match_score: float


class JobsListResponse(BaseModel):
    total: int
    jobs: list[JobResponse]


class RankedJobsListResponse(BaseModel):
    total: int
    jobs: list[RankedJobResponse]

app = FastAPI(title="Job Hunter API")


def convert_job_row(job):
    return {
        "id": job[0],
        "title": job[1],
        "company": job[2],
        "location": job[3],
        "url": job[4],
        "source": job[5],
        "job_id": job[6],
        "collected_at": job[7]
    }


@app.get("/")
def home():
    return {"message": "Job Hunter API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/jobs", response_model=JobsListResponse)
def list_jobs():
    rows = get_all_jobs()
    jobs = [convert_job_row(row) for row in rows]

    return {
        "total": len(jobs),
        "jobs": jobs
    }



@app.get("/ranked-jobs", response_model=RankedJobsListResponse)
def list_ranked_jobs(
    limit: int = Query(default=10, ge=1, le=100),
    company: str | None = None
):
    rows = get_all_jobs()
    profile = load_profile()

    jobs = []

    # Check whether the requested company exists
    if company:
        matching_company_exists = any(
            company.lower() in str(row[2]).lower()
            for row in rows
        )

        if not matching_company_exists:
            raise HTTPException(
                status_code=404,
                detail=f"No jobs found for company: {company}"
            )

    # Score and filter jobs
    for row in rows:
        job = convert_job_row(row)

        if company and company.lower() not in str(job["company"]).lower():
            continue

        score = score_job(job, profile)

        if score <= 0:
            continue

        job["match_score"] = score
        jobs.append(job)

    # Sort highest match scores first
    ranked_jobs = sorted(
        jobs,
        key=lambda job: job["match_score"],
        reverse=True
    )

    return {
        "total": len(ranked_jobs),
        "jobs": ranked_jobs[:limit]
    }