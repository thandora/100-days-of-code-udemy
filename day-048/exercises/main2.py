from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://www.facebook.com/"

driver = webdriver.Firefox()
driver.get(url=url)

input_email = driver.find_element(by=By.ID, value="email")
input_password = driver.find_element(by=By.ID, value="pass")
input_email.send_keys("foo_bar@mail.com")
input_password.send_keys("strongepassword")