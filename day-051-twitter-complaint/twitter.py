from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time

# Load env vars
load_dotenv(".env")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")

twitter_url = "https://twitter.com/"
driver = webdriver.Firefox()
driver.get(url=twitter_url)


def try_find(xpath: str) -> object:
    while True:
        try:
            print("Trying")
            x = driver.find_element(
                by=By.XPATH,
                value=xpath,
            )
            return x
        except NoSuchElementException:
            print("Retrying")
            time.sleep(1.5)


def login():
    button_login_twitter = try_find(
        "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a"
    )
    button_login_twitter.click()

    time.sleep(3.4)
    input_email = try_find(
        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
    )
    input_email.send_keys(TWITTER_EMAIL)
    input_email.send_keys(Keys.ENTER)
    time.sleep(1)

    input_pass = try_find(
        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
    )
    input_pass.send_keys(TWITTER_PASS)
    input_pass.send_keys(Keys.ENTER)

    time.sleep(3)
