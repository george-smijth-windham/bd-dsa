from functools import reduce


def count_marketers(job_titles):
    return len([title for title in job_titles if "marketer" == title.lower()])
