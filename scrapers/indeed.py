import requests
from config import JOB_TITLES, LOCATION
from urllib.parse import quote_plus


def search_jobs():
    job_title = JOB_TITLES[0]

    url = (
    f"https://in.indeed.com/jobs?"
    f"q={quote_plus(job_title)}&"
    f"l={quote_plus(LOCATION)}&"
    f"fromage=1"
)

    print("Search URL:")
    print(url)

    response = requests.get(url)

    print("Status code:", response.status_code)


if __name__ == "__main__":
    search_jobs()