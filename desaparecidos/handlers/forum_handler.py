from common.driver import driver
from utils import string_parser as parser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_LOGIN = "https://forocoches.com/foro/misc.php?do=page&template=ident"
URL_CREATE_THREAD = "https://forocoches.com/foro/newthread.php?do=newthread&f=2"
URL_THREAD = "https://forocoches.com/foro/showthread.php?p="


def login(username, password):
    driver.get(URL_LOGIN)

    wait = WebDriverWait(driver, 20)
    button_accept_cookies = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sd-cmp-JnaLO')))
    button_accept_cookies.click()

    input_username = driver.find_element(By.NAME, 'vb_login_username')
    input_password = driver.find_element(By.NAME, 'vb_login_password')
    button_submit = driver.find_element(By.XPATH, '//input[@value="Acceder"]')

    input_username.send_keys(username)
    input_password.send_keys(password)
    button_submit.click()


def create_thread(subject, body):
    driver.get(URL_CREATE_THREAD)

    input_subject = driver.find_element(By.NAME, 'subject')
    input_message = driver.find_element(By.NAME, 'message')
    button_submit = driver.find_element(By.NAME, 'sbutton')

    input_subject.send_keys(subject)
    input_message.send_keys(body)
    button_submit.click()

    post_id = parser.get_post_id(driver.current_url)
    return post_id


def reply_to_thread(thread_id, message):
    driver.get(URL_THREAD + str(thread_id))

    input_message = driver.find_element(By.ID, 'vB_Editor_QR_textarea')
    button_submit = driver.find_element(By.ID, 'qr_submit')

    input_message.send_keys(message)
    button_submit.click()

    post_id = parser.get_post_id(driver.current_url)
    return post_id
