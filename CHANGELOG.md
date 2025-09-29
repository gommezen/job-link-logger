# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-09-29
### Added
- Core pipeline: connect to Gmail via OAuth (`credentials.json` + `token.json`).
- Extract job links from Gmail (LinkedIn, Jobindex, lnkd.in).
- Collect metadata: Date, From, Subject, URL, Gmail Permalink.
- Save results in `job_links.xlsx` with status + notes columns.
- Track processed emails in `processed.json` to prevent duplicates.
- Command-line interface with:
  - `run` → run the pipeline
  - `doctor` → check config & files
  - Options: `--excel`, `--state`, `--query`, `--credentials`, `--token`, `--reset`, `--verbose`
- Pre-commit hooks with **Black**, **Flake8**, **Isort**.
- CI integration with GitHub Actions.
- Packaging via `pyproject.toml`.

### Changed
- Polished `README.md` with setup instructions, usage examples, and roadmap.

### Fixed
- Removed unused imports flagged by Flake8.
- Consistent formatting via Black.

---

## [Unreleased]
### Planned
- Config file support (`.env` / `config.toml`).
- Smarter defaults for Excel filenames (date suffix).
- `--dry-run` mode.
- Multiple Gmail queries.
- Excel enhancements (filters, job stats sheet).
- Notifications (Slack, Discord, Email).
- Optional web dashboard (Streamlit/FastAPI).
- Publish to **PyPI** and provide Docker support.
