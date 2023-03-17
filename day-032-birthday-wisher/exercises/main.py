import datetime as dt
import smtplib
import random

"""
Sends a random quote to an email every specific weekday. (Wednesday in this script)
"""
MY_EMAIL = "MY_EMAIL"
APP_PASSWORD = "MY_APP_PASSWORD"

to_email = "RECIPIENT_EMAIL"

now = dt.datetime.now()
weekday = now.weekday()
# Check if Wednesday
# 0 == Mon, 6 == Sun
if weekday == 2:

    # Select random quote.
    with open("quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes).strip()

    message = f"Subject:Weekly Quote\n\n{quote}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=message)

else:
    print(f"Quotes are only sent on Wednesdays. It's only {now.strftime('%A')}")
