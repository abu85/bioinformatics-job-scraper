import requests
from bs4 import BeautifulSoup

def scrape_glassdoor():
    url = "https://www.glassdoor.ca/Job/bioinformatics-jobs-SRCH_KO0,14.htm"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    jobs = []
    for card in soup.select("li.JobCard"):
        title = card.select_one("a[data-test='job-link']").text.strip()
        company = card.select_one("div[data-test='employer-name']").text.strip()
        link = "https://www.glassdoor.ca" + card.select_one("a")["href"]

        jobs.append({
            "site": "Glassdoor",
            "title": title,
            "company": company,
            "link": link
        })

    return jobs
