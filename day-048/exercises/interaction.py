from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Firefox()
driver.get(url=url)

article_count = driver.find_element(
    by=By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)"
)
print(article_count.text)
