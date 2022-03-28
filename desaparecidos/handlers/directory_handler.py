from common.driver import driver
from utils import string_parser as parser

from selenium.webdriver.common.by import By

URL_MISSING_PERSONS_DIRECTORY = "https://sosdesaparecidos.es/desaparecidos/"
URL_MISSING_PERSON_PROFILE = "https://sosdesaparecidos.es/desaparecido/"
URL_MISSING_PERSON_IMAGE = "https://sosdesaparecidos.es/wp-content/themes/sos-desaparecidos/carteles_foto/"


def get_all_missing_persons_urls():
    missing_persons_urls = driver.find_elements(By.CLASS_NAME, 'asp_res_url')
    while not missing_persons_urls or any(url.get_attribute('href') == ' ' for url in missing_persons_urls):
        missing_persons_urls = driver.find_elements(By.CLASS_NAME, 'asp_res_url')
    return missing_persons_urls


def get_all_missing_persons_ids():
    driver.get(URL_MISSING_PERSONS_DIRECTORY)
    missing_persons_urls = get_all_missing_persons_urls()
    missing_persons_ids = parser.get_missing_persons_ids_from_urls(missing_persons_urls)
    return missing_persons_ids


def get_missing_person_data(missing_person_id):
    driver.get(URL_MISSING_PERSON_PROFILE + missing_person_id)
    missing_since = get_missing_person_missing_since()
    location = get_missing_person_location()
    status = get_missing_person_status()
    return missing_since, location, status


def get_missing_person_missing_since():
    missing_since_text = driver.find_elements(By.CLASS_NAME, 'tag-info-fisica')[0]. \
        find_element(By.XPATH, '..').text.split(' ')[-1]
    return parser.parse_date(missing_since_text)


def get_missing_person_location():
    location = driver.find_elements(By.CLASS_NAME, 'tag-info-fisica')[2]. \
        find_element(By.XPATH, '..').text.split(':')[-1][1:]
    return location


def get_missing_person_status():
    found_labels = driver.find_elements(By.XPATH, '//span[@style = "font-size: 35px;background-color: ' +
                                                  '#00c;width: 100% !important;display: inline-block;"]')
    if found_labels:
        status = found_labels[0].text
    else:
        status = 'DESAPARECIDO'
    return status


def get_missing_person_image_url(missing_person_id):
    return URL_MISSING_PERSON_IMAGE + missing_person_id + ".jpg"
