from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import twitter

speed_url = "https://www.speedtest.net/"
# Deny location permission required by Speedtest.net
options = Options()
options.set_preference("geo.enabled", False)
options.set_preference("geo.prompt.testing", False)
options.set_preference("geo.prompt.testing.allow", False)

driver = webdriver.Firefox(options=options)
driver.get(speed_url)

# Speedtest
driver.find_element(by=By.CLASS_NAME, value="js-start-test.test-mode-multi").click()
time.sleep(20)

while True:
    try:
        dl_speed = driver.find_element(
            by=By.CLASS_NAME,
            value="result-data-large.number.result-data-value.download-speed",
        ).text
        dl_speed = float(dl_speed)

        ul_speed = driver.find_element(
            by=By.CLASS_NAME,
            value="result-data-large.number.result-data-value.upload-speed",
        ).text
        ul_speed = float(ul_speed)

        break

    except NoSuchElementException:
        time.sleep(3)
    except ValueError:
        time.sleep(3)

print(f"DOWN: {dl_speed}\nUP: {ul_speed}")

# Twitter
twitter.login()