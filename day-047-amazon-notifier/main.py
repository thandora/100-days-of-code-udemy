"""Monitors an item in amazon and sends a notification to user if the item's
price gets lower or equal to an asking price set by user through <WANTED_PRICE>
"""


from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

WANTED_PRICE = 100
product_page = "https://www.amazon.com/JOOLA-Tennis-Training-Oscillation-Wireless/dp/B016A7UMV8/ref=sr_1_5?crid=3TV3FPP4OQ6FE&keywords=table+tennis+robot&qid=1677625871&sprefix=table+tennis+robot%2Caps%2C271&sr=8-5"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-US,en;q=0.5",
}

r = requests.get(url=product_page, headers=header)
html = r.content

soup = BeautifulSoup(html, features="html.parser")
# Selects one of the elements containing the product's price
price = soup.select(".a-section.a-spacing-none.aok-align-center .a-offscreen")[
    0
].get_text()

price = float(price.strip("$"))
product_name = soup.find(name="span", id="productTitle").get_text()

if price <= WANTED_PRICE:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        # Message formatting. Blerg
        message = []
        message.append(
            f'Subject:Low Price!\n"{product_name.strip()}" is now on sale for '
        )
        message.append(f"${price}. It is below your asking price of ${WANTED_PRICE}")
        message.append(f"\n\nProduct page: {product_page}")
        message = "".join(message)

        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
        print("Current price is lower than wanted price. Notification sent.")
else:
    price("Current price is not lower than wanted price. No notification sent.")
