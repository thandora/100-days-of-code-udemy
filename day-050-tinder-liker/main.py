"""A selenium-based program that automatically logs in to Tinder
through an facebook account, and likes all users."""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from dotenv import load_dotenv
import os
import time

# Load env vars
load_dotenv(".env")
TINDER_GMAIL = os.getenv("TINDER_GMAIL")
TINDER_PASS = os.getenv("TINDER_PASS")

# Allows location permission required by Tinder
options = Options()
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", True)

# Set higher if slow internet speed
WAIT_BUFFER = 2

site = "https://tinder.com/"
driver = webdriver.Firefox(options=options)
driver.get(site)

# Login button
button_login = driver.find_element(
    by=By.XPATH,
    value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a",
)
button_login.click()

time.sleep(2 + WAIT_BUFFER)

button_fb_login = driver.find_element(
    by=By.XPATH,
    value="/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button",
)
button_fb_login.click()

# Login through FB
windows = driver.window_handles
window_fb_login = windows[1]
driver.switch_to.window(window_name=window_fb_login)

time.sleep(1 + WAIT_BUFFER)

input_email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
input_pass = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
input_email.send_keys(TINDER_GMAIL)
input_pass.send_keys(TINDER_PASS)

time.sleep(1)

button_login = driver.find_element(
    by=By.NAME,
    value="login",
)
button_login.click()

time.sleep(4)

driver.switch_to.window(window_name=windows[0])

# Allow permissions
button_allow_location = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/main/div/div/div/div[3]/button[1]"
)

button_allow_location.click()
time.sleep(1.5)
button_deny_notification = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/main/div/div/div/div[3]/button[2]"
)

button_deny_notification.click()
button_accept_cookies = driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button"
)

time.sleep(2)

button_accept_cookies.click()

# Get match button element
while True:
    try:
        button_match = driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button",
        )
    except NoSuchElementException:
        time.sleep(1)
    else:
        break


for _ in range(100):
    time.sleep(1)
    try:
        print("Matching")
        button_match.click()
    except NoSuchElementException:
        time.sleep(1)
    except ElementClickInterceptedException:
        print("Found a match.")
        button_back = driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button",
        )
        button_back.click()
    else:
        print("Liked. Finding next.")
