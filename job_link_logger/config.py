# job_link_logger/config.py
import os

try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    pass

APP_DIR = os.path.expanduser("~/.config/job-link-logger")
os.makedirs(APP_DIR, exist_ok=True)

CREDENTIALS_PATH = os.getenv(
    "CREDENTIALS_PATH",
    os.path.join(APP_DIR, "credentials.json"),
)
TOKEN_PATH = os.getenv(
    "TOKEN_PATH",
    os.path.join(APP_DIR, "token.json"),
)

LABEL_NAME = os.getenv("LABEL_NAME", "Jobs/LinkedIn")
EXCEL_PATH = os.getenv("EXCEL_PATH", "job_links.xlsx")
STATE_PATH = os.getenv("STATE_PATH", "processed.json")
DAYS = int(os.getenv("DAYS", "60"))

SEARCH_TERMS = ["linkedin.com/jobs", "lnkd.in/", "jobindex.dk/vis-job"]
_terms = " OR ".join(f'"{t}"' for t in SEARCH_TERMS)
GMAIL_QUERY = f'(label:"{LABEL_NAME}" OR ({_terms})) newer_than:{DAYS}d'
