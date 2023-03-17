"""Using selenium, store the upcoming events in a dict from python.org
Site: https://www.python.org/
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint


test_url = "https://www.python.org/"

driver = webdriver.Firefox()
driver.get(test_url)

# Get div that holds the unordered list the events are placed in.
list_container = driver.find_element(
    by=By.XPATH,
    value="/html/body/div/div[3]/div/section/div[2]/div[2]",
)

# Get the list elements which contains events date and name.
list_elements = list_container.find_elements(by=By.CSS_SELECTOR, value="li")

# Store in dict
events = {}
for i, element in enumerate(list_elements):
    date = element.find_element(by=By.CSS_SELECTOR, value="time").text
    event = element.find_element(by=By.CSS_SELECTOR, value="a").text
    events[i] = {
        "time": date,
        "name": event,
    }

pprint(events)

driver.quit()
