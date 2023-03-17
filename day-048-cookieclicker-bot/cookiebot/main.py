"""Uses selenium to play classic cookie clicker game on: 
http://orteil.dashnet.org/experiments/cookie/
The program clicks the cookie 5 times, and then check to see if it can upgrade
anything, if it can, it will upgrade the most expensive upgrade.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

RUN_IN_MINS = 20

game_url = "https://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Firefox()
driver.get(url=game_url)

money = float(driver.find_element(by=By.ID, value="money").text)
cookie = driver.find_element(by=By.ID, value="cookie")


def init_upgrades() -> list:
    """# Initialize a list of upgrade properties in dict form:
     {
       "name": <upgrade_name>,
       "web_element": [<selenium_web_element>, <html_id>],
       "cost": <current_upgrade_cost>,
     }

    Returns:
        list: List of properties
    """

    upgrades_db = []

    upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

    for upgrade in upgrades:
        element = upgrade.find_element(by=By.TAG_NAME, value="b")
        text = element.text

        try:
            name = text.split()[0]
            price = text.split()[-1]
            # Convert comma delimited number to float
            price = float(price.replace(",", ""))
            html_id = upgrade.get_attribute("id")
            upgrades_db.append(
                {"name": name, "cost": price, "web_element": [element, html_id]}
            )
        except IndexError:
            continue

    return upgrades_db


def update_price(upgrades_list: list, html_id: str) -> None:
    """Update an entry's cost information inside <upgrades_list>.

    Args:
        upgrades_list (list): list of dicts containing upgrade information
        html_id (str): html id of upgrade to be updated.
    """

    for upgrade in upgrades_list:
        if upgrade["web_element"][1] == html_id:
            new_element = driver.find_element(by=By.ID, value=html_id)
            new_element = new_element.find_element(by=By.TAG_NAME, value="b")
            upgrade["web_element"][0] = new_element

            new_cost = new_element.text.split()[-1]
            new_cost = float(new_cost.replace(",", ""))
            upgrade["cost"] = new_cost

            break


def sort_price(upgrades_list: list) -> None:
    """Sorts <upgrades_list> in descending order of cost.

    Args:
        upgrades_list (list): list of upgrades.
    """
    upgrades_list.sort(reverse=True, key=lambda e: e.get("cost"))


def upgrade(money: float, sorted_upgrades_list: list) -> bool:
    """Upgrades most expensive upgrade in <sorted_upgrades_list>.

    Args:
        money (float): current number of cookies.
        sorted_upgrades_list (list): list of upgrades in descending order of cost.

    Returns:
        bool: True if upgrade successful. False otherwise.
    """
    for upgrade in sorted_upgrades_list:
        cost = upgrade["cost"]
        upgrade_id = upgrade["web_element"][1]
        upgrade_name = upgrade["name"]

        upgrade_element = driver.find_element(by=By.ID, value=upgrade_id)
        upgrade_element = upgrade_element.find_element(by=By.TAG_NAME, value="b")

        if money >= cost:
            upgrade_element.click()
            print(f"{upgrade_name} upgraded.")
            update_price(upgrades_list=sorted_upgrades_list, html_id=upgrade_id)
            return True

    return False


# Initialize upgrades data structure.
upgrades_db = init_upgrades()

# Run for <RUN_IN_MINS> mins.
time_end = time.time() + (60 * RUN_IN_MINS)
while time.time() < time_end:

    time.sleep(1)
    for _ in range(5):
        cookie.click()

    money = float(driver.find_element(by=By.ID, value="money").text)
    sort_price(upgrades_list=upgrades_db)
    upgrade(money=money, sorted_upgrades_list=upgrades_db)
