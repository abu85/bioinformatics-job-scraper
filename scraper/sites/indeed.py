import requests
from bs4 import BeautifulSoup

def scrape_indeed():
    url = "https://ca.indeed.com/jobs?q=bioinformatics&l="
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    jobs = []
    for card in soup.select("div.job_seen_beacon"):
        title = card.select_one("h2").text.strip()
        company = card.select_one(".companyName").text.strip() if card.select_one(".companyName") else "N/A"
        link = "https://ca.indeed.com" + card.select_one("a")["href"]

        jobs.append({
            "site": "Indeed",
            "title": title,
            "company": company,
            "link": link
        })

    return jobs
