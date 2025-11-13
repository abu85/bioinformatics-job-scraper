import json
from sites.indeed import scrape_indeed
from sites.glassdoor import scrape_glassdoor
from sites.simplyhired import scrape_simplyhired

def main():
    all_jobs = []

    print("Scraping Indeed...")
    all_jobs.extend(scrape_indeed())

    print("Scraping Glassdoor...")
    all_jobs.extend(scrape_glassdoor())

    print("Scraping SimplyHired...")
    all_jobs.extend(scrape_simplyhired())

    # Save jobs to website folder
    with open("../website/jobs.json", "w") as outfile:
        json.dump(all_jobs, outfile, indent=4)

    print("Saved jobs to ../website/jobs.json")

if __name__ == "__main__":
    main()
