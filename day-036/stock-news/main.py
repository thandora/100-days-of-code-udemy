import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import smtplib

"""
Send's notification of recent change of a stock price
(close price from yesterday compared to the day before yesterday)
to an email. Also show 3 most popular articles mentioning the stock.
"""


def delta_format(value: float) -> None:
    """Return str of %delta change of value relative to 0.

    Args:
        value (float): value to be determined if positive change or negative
    """
    if value > 0:
        s = "🔺{value}%"
    elif value < 0:
        s = f"🔻{abs(value)}%"
    else:
        s = "- 0%"

    return s


# .env
load_dotenv(".env")
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
my_email = os.getenv("MY_EMAIL")
my_app_pass = os.getenv("APP_PASSWORD")

STOCK_SYM = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_ep = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "IBM",
    "outputsize": "compact",
    "apikey": stock_api_key,
}

r = requests.get(url=stock_ep, params=stock_parameters)
r.raise_for_status()
stocks_data = r.json()

today = datetime.today().date()
yesterday = today - timedelta(days=1)
two_yesterday = today - timedelta(days=2)
data_series = stocks_data["Time Series (Daily)"]

# Cast to string
yesterday = str(yesterday)
two_yesterday = str(two_yesterday)

# Closing prices
yest_cl = float(data_series[yesterday]["4. close"])
tyest_cl = float(data_series[two_yesterday]["4. close"])

# Per cent change: (new - old) / (old)
change = (yest_cl - tyest_cl) / tyest_cl
change = round(change * 100, 1)

news_ep = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": "tesla",
    "from": two_yesterday,
    "to": yesterday,
    "sortBy": "popularity",
    "apiKey": news_api_key,
    "pageSize": 3,
}

# Parse articles
news_response = requests.get(url=news_ep, params=news_parameters)
news_response.raise_for_status()
articles = news_response.json()["articles"]

# Format articles
messages = []
for article in articles:
    change_format = delta_format(change)
    message = f"{STOCK_SYM}:{change_format}%\n"
    message_body = f"Headline: {article['title']}\n" f"Brief: {article['description']}"
    messages.append(message_body)
messages.insert(0, message)

# Send news
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    message = "\n\n".join(messages)
    message = (f"Subject:{STOCK_SYM} NEWS\n\n" + message).encode("utf-8")

    connection.starttls()
    connection.login(user=my_email, password=my_app_pass)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)
