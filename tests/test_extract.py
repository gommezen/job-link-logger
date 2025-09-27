from job_link_logger.cli import extract_job_urls

def test_linkedin_plain():
    urls = extract_job_urls("x", "https://www.linkedin.com/jobs/view/4300000000", "")
    assert urls == ["https://www.linkedin.com/jobs/view/4300000000"]

def test_trailing_chars_trimmed():
    urls = extract_job_urls("x", "… https://www.linkedin.com/jobs/view/4300000000> end", "")
    assert urls == ["https://www.linkedin.com/jobs/view/4300000000"]

def test_lnkd_shortlink():
    urls = extract_job_urls("x", "ln: https://lnkd.in/abcd-XYZ", "")
    assert urls == ["https://lnkd.in/abcd-XYZ"]

def test_jobindex():
    urls = extract_job_urls("x", "IT-chef: https://www.jobindex.dk/vis-job/h1593572", "")
    assert urls == ["https://www.jobindex.dk/vis-job/h1593572"]

def test_html_anchor():
    html = '<a href="https://www.linkedin.com/jobs/view/4302962636?tracking=abc">Job</a>'
    urls = extract_job_urls("", "", html)
    assert urls == ["https://www.linkedin.com/jobs/view/4302962636"]
