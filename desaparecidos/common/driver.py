from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
             "AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/87.0.4280.88 Safari/537.36"


def set_driver():
    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("user-agent=" + USER_AGENT)

    driver = webdriver.Chrome(options=options)
    return driver


driver = set_driver()
