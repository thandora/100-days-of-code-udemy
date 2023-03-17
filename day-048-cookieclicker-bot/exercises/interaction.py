from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Firefox()
driver.get(url=url)

article_count = driver.find_element(
    by=By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)"
)

search_bar = driver.find_element(by=By.NAME, value="search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
