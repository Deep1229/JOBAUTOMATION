import requests

url = "https://boards-api.greenhouse.io/v1/boards/stripe/jobs?content=true"

response = requests.get(url)

print(response.status_code)
data = response.json()

print(type(data))
print(data.keys())
jobs = data["jobs"]

print(len(jobs))
#print(jobs[0])
#print(jobs[0].keys())
print(jobs[0]["title"])
job = jobs[0]
print(jobs[0]["location"])
print("Location:", job["location"]["name"])
print("URL:", job["absolute_url"])
print("Description:", job["content"][:200])