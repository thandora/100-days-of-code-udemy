"""Scrapes listing data from Zillow and enter them into a google form.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from typing import Iterable
from datascraper import DataScraper
import os
import time


def submit(listing_details: Iterable, form_link: str, n: int = -1) -> None:
    """Submits the information in <listing_details> into a google form.

    Args:
        listing_details (Iterable): iterable of listing information
        form_link (str): link to a google form with 3 inputs in order of:
        unit address, unit price, and url to unit.
        n (int, optional): Number of forms to submit. Can't be more than
        len(listing_details). Defaults to -1, meaning to submit everything.
    """

    driver = webdriver.Firefox()

    form_link = form_link

    if n == -1:
        listings = listing_details
    else:
        listings = listing_details[:n]

    n_items = len(listings)

    for i, listing in enumerate(listings):
        # Locate HTML inputs and enter corresponding details.
        time.sleep(2)
        driver.get(url=form_link)
        time.sleep(1)
        input_address = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
        )
        input_price = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
        )
        input_link = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
        )
        input_address.send_keys(listing["location"])
        input_price.send_keys(listing["price"])
        input_link.send_keys(listing["link"])
        button_submit = driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span",
        )
        button_submit.click()
        print(f"Submitted ({i+1}/{n_items})")


# Load env vars
load_dotenv(".env")
form_link = os.getenv("FORM_LINK")
zillow_listings_url = os.getenv("ZILLOW_LISTINGS")

scraper = DataScraper(zillow_list_url=zillow_listings_url)
listing_elements = scraper.get_elements()
listings = scraper.get_details(listing_elements=listing_elements)
submit(listing_details=listings, form_link=form_link, n=3)
