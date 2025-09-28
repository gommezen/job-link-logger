# Job Link Logger

![CI](https://github.com/YOURUSERNAME/job-link-logger/actions/workflows/ci.yml/badge.svg)


A small Python utility that automatically collects **LinkedIn job links** from Gmail
and logs them into an Excel file for easy tracking.

---

## Features
- Uses the Gmail API (read-only scope).
- Extracts `linkedin.com/jobs/...` and `lnkd.in/...` links from labeled emails.
- Appends to `job_links.xlsx` with columns:
  - Date  
  - From  
  - Subject  
  - LinkedIn URL  
  - Gmail Permalink  
  - Status (dropdown: To Review, Applied, Interview, Offer, Rejected, On Hold)  
  - Notes
- Prevents duplicates and remembers processed emails.
- Optional: schedule with Task Scheduler (Windows) or `cron` (Linux/macOS).

---

## Setup

### 1. Clone and install
```bash
git clone https://github.com/YOURUSERNAME/job-link-logger.git
cd job-link-logger
python -m venv .venv

# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install --upgrade pip
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib openpyxl html2text

### 2. Create Google OAuth credentials

Go to Google Cloud Console
.

Create or select a project.

Enable the Gmail API.

Configure the OAuth consent screen:

User type: External

Add your Gmail as a test user.

Create an OAuth Client ID:

Application type: Desktop app

Download the JSON and save it in this project as credentials.json

⚠️ Never commit credentials.json or token.json to GitHub (they’re ignored via .gitignore).


### 3. Prepare Gmail

In Gmail, create a label, e.g. Jobs/LinkedIn.

Create a filter so that LinkedIn job emails (e.g., with [JOB] in the subject) are automatically labeled.

Confirm in Gmail that your job emails appear under this label.

### 4. Run the script
python job_link_logger.py


On the first run, a browser window will open.

Log in with the Gmail you added as a test user.

Approve the read-only access.

A token.json file will be created for future runs.

Your job links will now be extracted and saved in job_links.xlsx.