import os
from dotenv import load_dotenv

load_dotenv()

LABEL_NAME = os.getenv("LABEL_NAME", "Jobs/LinkedIn")
EXCEL_PATH = os.getenv("EXCEL_PATH", "job_links.xlsx")
STATE_PATH = os.getenv("STATE_PATH", "processed.json")
DAYS = int(os.getenv("DAYS", "60"))

SEARCH_TERMS = ["linkedin.com/jobs", "lnkd.in/", "jobindex.dk/vis-job"]
_terms = " OR ".join(f'"{t}"' for t in SEARCH_TERMS)
GMAIL_QUERY = f'(label:"{LABEL_NAME}" OR ({_terms})) newer_than:{DAYS}d'
