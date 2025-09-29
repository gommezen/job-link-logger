from pathlib import Path
import tomllib  # Python 3.11+ has this built in

from job_link_logger.config import (
    EXCEL_PATH as EXCEL_PATH_DEFAULT,
    STATE_PATH as STATE_PATH_DEFAULT,
    GMAIL_QUERY as GMAIL_QUERY_DEFAULT,
    CREDENTIALS_PATH as CREDENTIALS_DEFAULT,
    TOKEN_PATH as TOKEN_DEFAULT,
)

CONFIG_FILE = "job-link-logger.toml"

DEFAULTS = {
    "excel": str(EXCEL_PATH_DEFAULT),
    "state": str(STATE_PATH_DEFAULT),
    "query": GMAIL_QUERY_DEFAULT,
    "credentials": str(CREDENTIALS_DEFAULT),
    "token": str(TOKEN_DEFAULT),
    "reset": False,
}


def load_config():
    """
    Load config from job-link-logger.toml if it exists.
    CLI flags override config file values.
    """
    path = Path(CONFIG_FILE)
    if not path.exists():
        return DEFAULTS.copy()

    with open(path, "rb") as f:
        data = tomllib.load(f)

    cfg = DEFAULTS.copy()
    cfg.update(data.get("job_link_logger", {}))
    return cfg
