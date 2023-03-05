from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
from random import uniform


class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()

    def login(self):
        # Load env vars
        load_dotenv(".env")
        IG_USER = os.getenv("IG_USER")
        IG_PASS = os.getenv("IG_PASS")

        instagram_url = "https://www.instagram.com/"
        self.driver.get(url=instagram_url)

        while True:
            try:
                input_username = self.driver.find_element(by=By.NAME, value="username")
                input_username.send_keys(IG_USER)
                break
            except NoSuchElementException:
                time.sleep(1)

        input_password = self.driver.find_element(by=By.NAME, value="password")
        input_password.send_keys(IG_PASS)
        input_password.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            button_dont_remember = self.driver.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button",
            )
            button_dont_remember.click()

        except NoSuchElementException:
            pass

        time.sleep(2)

        try:
            button_notif_off = self.driver.find_element(
                by=By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
            )
            button_notif_off.click()

        except NoSuchElementException:
            pass

        time.sleep(5)

    def find_follower(self):
        # Load env vars
        load_dotenv(".env")
        IG_SIMILAR_ACC = os.getenv("SIMILAR_ACC")

        button_search = self.try_find(
            xpath="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a"
        )
        button_search.click()

        time.sleep(2.5)

        input_search = self.try_find(
            xpath="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input"
        )
        input_search.send_keys(IG_SIMILAR_ACC)
        time.sleep(2)

        # First enter is to select first search result.
        input_search.send_keys(Keys.ENTER)
        input_search.send_keys(Keys.ENTER)
        time.sleep(5)

    def follow(self):
        followers_panel = self.try_find(
            xpath="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div"
        )
        followers_panel.click()
        time.sleep(5)
        buttons_follower = self.driver.find_elements(
            by=By.CSS_SELECTOR, value="._aano > div:nth-child(2) button"
        )
        for button in buttons_follower:
            status = button.find_element(
                by=By.CSS_SELECTOR, value="div div"
            ).text.lower()

            # Skip followed or requested accounts.
            if status != "follow":
                continue

            button.click()
            time.sleep(uniform(1.1, 2.5))

    def try_find(self, xpath: str) -> object:
        while True:
            try:
                print("Trying")
                x = self.driver.find_element(
                    by=By.XPATH,
                    value=xpath,
                )
                return x
            except NoSuchElementException:
                print("Retrying")
                time.sleep(1.5)


ig = InstaFollower()
ig.login()
ig.find_follower()
ig.follow()
