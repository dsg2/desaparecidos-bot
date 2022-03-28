import re
from datetime import date


def get_post_id(post_url):
    return re.findall(r'\d+', post_url)[-1]


def get_missing_persons_ids_from_urls(missing_persons_urls):
    missing_persons_ids = []
    for url in missing_persons_urls:
        missing_persons_ids.append(get_missing_person_id_from_url(url.get_attribute('href')))
    return missing_persons_ids


def get_missing_person_id_from_url(missing_person_url):
    return re.findall(r'([^\/]+$)', missing_person_url[:-1])[0]


def parse_date(date_string):
    split_date = date_string.split('/')
    return date(int(split_date[2]), int(split_date[1]), int(split_date[0]))
