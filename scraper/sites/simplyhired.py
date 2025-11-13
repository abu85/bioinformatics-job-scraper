import requests
from bs4 import BeautifulSoup

def scrape_simplyhired():
    url = "https://www.simplyhired.ca/search?q=bioinformatics"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    jobs = []
    cards = soup.select("div.SerpJob-jobCard")
    for card in cards:
        title = card.select_one("a.SerpJob-link").text.strip()
        company = card.select_one("span.JobPosting-labelWithIcon").text.strip()
        link = "https://www.simplyhired.ca" + card.select_one("a")["href"]

        jobs.append({
            "site": "SimplyHired",
            "title": title,
            "company": company,
            "link": link
        })

    return jobs
