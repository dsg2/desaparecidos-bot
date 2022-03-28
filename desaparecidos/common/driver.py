from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def set_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


driver = set_driver()
