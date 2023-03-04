from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
from datetime import datetime

load_dotenv(".env")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")
TWITTER_USER = os.getenv("TWITTER_USER")


class Twitter:
    def __init__(self, speeds: list, driver: object) -> None:
        self.down_speed = speeds[0]
        self.up_speed = speeds[1]
        self.driver = driver
        # Load env vars

    def login(self):
        button_login_twitter = self.try_find(
            "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a"
        )
        button_login_twitter.click()

        time.sleep(3.4)
        input_email = self.try_find(
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
        )
        input_email.send_keys(TWITTER_EMAIL)
        input_email.send_keys(Keys.ENTER)
        time.sleep(1)

        try:
            confirmation = self.driver.find_element(
                by=By.XPATH,
                value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
            )
        except NoSuchElementException:
            pass
        else:
            confirmation.send_keys(TWITTER_USER)
            confirmation.send_keys(Keys.ENTER)
            time.sleep(1)

        input_pass = self.try_find(
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
        )
        input_pass.send_keys(TWITTER_PASS)
        input_pass.send_keys(Keys.ENTER)

        time.sleep(3)

    def post(self):
        compose_tweet = self.try_find(
            "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a"
        )
        compose_tweet.click()

        time.sleep(1)
        # input_tweet = try_find(
        #     "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div"
        # )
        # input_tweet.send_keys(
        #     f"I have speeds of: {self.down_speed} down/{self.up_speed} up."
        # )
        x = self.driver.switch_to.active_element

        now = datetime.now()
        now_format = now.strftime("%Y-%m-%d, %H:%M")
        x.send_keys(
            f"{now_format}: I have speeds of: {self.down_speed} down/{self.up_speed} up."
        )

        time.sleep(2)
        self.try_find(
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span"
        ).click()
        print('Tweeted!')

    def load_page(self):
        twitter_url = "https://twitter.com/"

        self.driver.get(url=twitter_url)

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
