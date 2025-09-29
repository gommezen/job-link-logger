# Job Link Logger

![CI](https://github.com/gommezen/job-link-logger/actions/workflows/ci.yml/badge.svg)

A small Python utility that automatically collects **job links** (e.g. LinkedIn, Jobindex.dk, `lnkd.in`) from Gmail and logs them into an Excel file for easy tracking.  

---

## ✨ Features
- Connects to Gmail via **OAuth** (read-only).
- Extracts job links and metadata:
  - Date  
  - From  
  - Subject  
  - Job URL  
  - Gmail Permalink  
  - Status (dropdown: To Review, Applied, Interview, Offer, Rejected, On Hold)  
  - Notes
- Prevents duplicates (tracks processed emails in `processed.json`).
- Appends unique jobs to `job_links.xlsx`.
- Ready-to-use **CLI** with multiple options.
- Tested, linted (Flake8/Black/Isort), and CI-integrated.  

---

## 🚀 Quickstart

### 1. Clone & Install
```bash
git clone https://github.com/gommezen/job-link-logger.git
cd job-link-logger
python -m venv .venv

# Activate virtualenv
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install --upgrade pip
pip install -e .
```

---

### 2. Create Google OAuth Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/).  
2. Create or select a project.  
3. Enable the **Gmail API**.  
4. Configure the OAuth consent screen:  
   - User type: **External**  
   - Add your Gmail as a test user  
5. Create an OAuth Client ID:  
   - Application type: **Desktop app**  
6. Download the JSON → save it as **`credentials.json`** in this project.  

⚠️ **Never commit** `credentials.json` or `token.json`. They’re already in `.gitignore`.

---

### 3. Prepare Gmail
- Create a label in Gmail, e.g. `Jobs/LinkedIn`.  
- Add filters so LinkedIn/Jobindex job emails are tagged with this label.  
- Confirm in Gmail that job mails appear under this label.  

---

### 4. Run the Logger
```bash
# First run: will open browser for OAuth
python -m job_link_logger run --verbose
```

This will:  
- Authenticate your Gmail.  
- Extract job links.  
- Save them in `job_links.xlsx`.  

---

## 🛠 CLI Commands

```bash
python -m job_link_logger run         # Run pipeline
python -m job_link_logger doctor      # Check setup & files
```

### Options
- `--excel PATH` → custom Excel filename  
- `--state PATH` → custom state file  
- `--query QUERY` → custom Gmail search  
- `--credentials PATH` / `--token PATH` → custom auth files  
- `--reset` → reset processed state  
- `--verbose` → extra debug output  

---

## 📈 Roadmap (v0.2+)
- Config via `.env` / `config.toml` (no more long CLI args).  
- Smarter defaults (Excel with date suffixes).  
- `--dry-run` mode (show jobs, no write).  
- Multi-query support (LinkedIn + Jobindex + custom).  
- Excel enhancements (filters, job stats sheet).  
- Notifications (Slack, Discord, Email).  
- Optional web dashboard (Streamlit/FastAPI).  
- Publish to **PyPI** + Docker support.  

---

## 📜 License
MIT License © 2025 Niels Gommesen