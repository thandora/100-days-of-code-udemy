from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

# Load env vars
load_dotenv(".env")
acc_email = os.getenv("ACC_EMAIL")
acc_pass = os.getenv("ACC_PASS")


site = "https://www.linkedin.com/"

driver = webdriver.Firefox()
driver.get(url=site)

input_email = driver.find_element(by=By.NAME, value="session_key")
input_pass = driver.find_element(by=By.NAME, value="session_password")
button_signin = driver.find_element(
    by=By.CLASS_NAME,
    value="btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width",
)

# Sign in
input_email.send_keys(acc_email)
time.sleep(0.5)
input_pass.send_keys(acc_pass)
time.sleep(0.2)
button_signin.click()
time.sleep(6.5)


# Nav to jobs and search
jobs_tab = driver.find_element(
    by=By.XPATH, value="/html/body/div[5]/header/div/nav/ul/li[3]/a"
)
print(jobs_tab)
jobs_tab.click()

time.sleep(2)


# Search
input_search = driver.find_element(
    by=By.ID,
    value="jobs-search-box-keyword-id-ember225",
)
search_query = "data engineer"
input_search.send_keys(search_query)
input_search.send_keys(Keys.ENTER)

time.sleep(5)
location_type = driver.find_element(
    by=By.XPATH,
    value="/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/span/button",
)
location_type.click()

remote_type = driver.find_element(
    by=By.XPATH,
    value="/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[2]/label/p/span[1]",
)

remote_type.click()
time.sleep(2)
apply_remote_filter = driver.find_element(
    by=By.CSS_SELECTOR, value=".scaffold-layout__list-header"
)

apply_remote_filter.click()

# Select first three results
results = driver.find_elements(
    by=By.CSS_SELECTOR, value=".scaffold-layout__list-container li"
)[:3]

# Save results
for result in results:
    results.click()
    time.sleep(5)
    # TODO SAVE JOB
print(results)
