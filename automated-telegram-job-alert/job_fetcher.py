import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil import parser
from config import ROLES, SITES

def fetch_jobs():
    jobs = []
    now = datetime.now()

    for role in ROLES:
        query = role.replace(' ', '%20')

        for site in SITES:
            site_jobs = []

            if site == "linkedin":
                url = f"https://www.linkedin.com/jobs/search/?keywords={query}&f_TPR=r86400"  # 24 hours
                headers = {"User-Agent": "Mozilla/5.0"}
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, "lxml")

                for job_card in soup.find_all("a", {"class":"base-card__full-link"}):
                    title = job_card.get_text(strip=True)
                    link = job_card["href"]
                    time_tag = job_card.find_next("time")
                    if time_tag:
                        posted = time_tag.get("datetime")
                        if posted:
                            try:
                                posted_dt = parser.parse(posted)
                            except:
                                continue
                            # 24-hour filter
                            if now - posted_dt <= timedelta(hours=24):
                                site_jobs.append(f" Last 24 Hours\n Role: {role}\n LinkedIn\n {link}")

            elif site == "naukri":
                url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs"
                headers = {"User-Agent": "Mozilla/5.0"}
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, "lxml")

                for job_card in soup.find_all("article", {"class": "jobTuple"}):
                    title_tag = job_card.find("a", {"class":"title"})
                    if title_tag and role.lower() in title_tag.get_text(strip=True).lower():
                        link = title_tag["href"]
                        time_tag = job_card.find("time")
                        if time_tag:
                            posted_text = time_tag.get_text(strip=True)
                            # check if posted within 24 hours
                            if "hr" in posted_text.lower() or "hrs" in posted_text.lower() or "1 day" in posted_text.lower():
                                site_jobs.append(f" Last 24 Hours\n Role: {role}\n Naukri\n {link}")

            elif site == "unstop":
                url = f"https://unstop.com/jobs?query={query}"
                headers = {"User-Agent": "Mozilla/5.0"}
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, "lxml")

                for job_card in soup.find_all("a", {"class": "job-card"}):
                    title_tag = job_card.find("h3")
                    if title_tag and role.lower() in title_tag.get_text(strip=True).lower():
                        link = job_card["href"]
                        posted_tag = job_card.find("span", {"class":"posted-time"})
                        if posted_tag:
                            posted_text = posted_tag.get_text(strip=True)
                            if "hr" in posted_text.lower() or "1 day" in posted_text.lower():
                                site_jobs.append(f"Last 24 Hours\n Role: {role}\n Unstop\n {link}")

            elif site == "wellfound":
                url = f"https://wellfound.com/jobs?search={query}"
                headers = {"User-Agent": "Mozilla/5.0"}
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, "lxml")

                for job_card in soup.find_all("a", {"class": "job-card"}):
                    title_tag = job_card.find("h3")
                    if title_tag and role.lower() in title_tag.get_text(strip=True).lower():
                        link = job_card["href"]
                        posted_tag = job_card.find("span", {"class":"posted-time"})
                        if posted_tag:
                            posted_text = posted_tag.get_text(strip=True)
                            if "hr" in posted_text.lower() or "1 day" in posted_text.lower():
                                site_jobs.append(f"Last 24 Hours\n Role: {role}\n Wellfound\n {link}")

            jobs.extend(site_jobs)

    return "\n\n".join(jobs)
