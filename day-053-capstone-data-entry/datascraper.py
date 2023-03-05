"""Contains the DataScraper class responsible for scraping data of Zillow,
and organizing them into a structured list.
"""


from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from typing import Iterable
import os

# Load env var
load_dotenv(".env")
zillow_list_url = os.getenv("ZILLOW_LISTINGS")


class DataScraper:
    """Class responsible for scraping and organizing data off Zillow."""

    def __init__(self, zillow_list_url) -> None:
        self.zillow_list_url = zillow_list_url

    def get_elements(self) -> list:
        """Scrapes listings from Zillow filtered by <zillow_list_url> and
        returns list of soup tags.

        Returns:
            list: list of listings of type soup element tags.
        """

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
            "Accept-Language": "en-US,en;q=0.5",
        }

        # GET request for page HTML
        r = requests.get(url=self.zillow_list_url, headers=header)
        r.raise_for_status()
        html = r.text

        soup = BeautifulSoup(html, features="html.parser")
        # Weird class name. Might be periodically changed.
        listings = soup.select(selector=".List-c11n-8-85-1__sc-1smrmqp-0 li")
        return listings

    def get_details(self, listing_elements: Iterable) -> list:
        """Organize and store relevant information from provided list of soup elements.

        Args:
            listing_elements (Iterable): iter containing listing soup elements.

        Returns:
            list: list of dicts in the form of:
                [   {
                    "location": <address>,
                    "price": <unit price>,
                    "link": <link to unit>,
                    },
                    {Data n},
                ]
        """
        listings = []
        for item in listing_elements:

            try:
                price_text = item.select_one(selector="article div span").text
                address_text = item.select_one(selector="address").text
                link_text = item.select_one(selector="a")["href"]

                # IDK why their href structure is not consistent. Anti-scrape maybe?
                if "zillow.com" not in link_text:
                    link_text = "https://www.zillow.com" + link_text

            except AttributeError:
                continue

            else:
                # Clean price data.
                if "+" in price_text:
                    price_text = price_text.split("+")[0]

                else:
                    price_text = price_text.split("/")[0]

                price = int(price_text[1:].replace(",", ""))

                listing = {
                    "location": address_text,
                    "price": price,
                    "link": link_text,
                }

                listings.append(listing)

        return listings
