import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()


def test_adzuna():
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": 10,
        "what": "Data Engineer",
        "where": "Bangalore",
        "sort_by": "date",
        "max_days_old": 1,
    }

    response = requests.get(url, params=params)

    print("Status code:", response.status_code)

    data = response.json()

    for job in data["results"]:
            print("Job:", job["title"])
            print("Created:", job["created"])
            posted_at = datetime.fromisoformat(
            job["created"].replace("Z", "+00:00")
    )
            

            
            print("Title:", job["title"])
            print("Company:", job["company"]["display_name"])
            print("Location:", job["location"]["display_name"])
            print("URL:", job["redirect_url"])
            print("Posted:", posted_at)
            
            print("---")


if __name__ == "__main__":
    test_adzuna()