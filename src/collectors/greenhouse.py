import requests


def get_greenhouse_jobs(board_token):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    return data["jobs"]