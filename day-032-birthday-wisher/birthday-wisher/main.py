import datetime as dt
import pandas as pd
import random
import smtplib
from pprint import pprint

"""
Sends a birthday greeting to a celebrant if it's their birthday today.
The program takes a random template from letter_templates/

"""
MY_EMAIL = "MY_EMAIL"
APP_PASSWORD = "MY_APP_PASS"

# Today's month and day
now = dt.datetime.now()
now_md = (now.month, now.day)

birthdays_df = pd.read_csv("birthdays.csv")
birthdays = {}
celebrants = []

# Create a dict for birthdays in the form:
# {
#  (month, day): [celebrant1, celebrant2],
# }
birthdays = {}
for _, info in birthdays_df.iterrows():
    birthday = (info["month"], info["day"])

    if birthday in birthdays:
        birthdays[birthday].append(info)
    else:
        birthdays[birthday] = [info]

celebrants = birthdays.get(now_md)

# Check if anyone is having their birthday today.
# "if celebrants" is shorter, but this is arguably more readable.
if len(celebrants) > 0:

    # Send greetings for each celebrant
    for celebrant in celebrants:
        template_path = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"

        with open(template_path) as f:
            template = f.read()
            birthday_message = template.replace("[NAME]", celebrant["name"])

        message = f"Subject:Happy Birthday!\n\n{birthday_message}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs=celebrant["email"], msg=message
            )

            print(f"Sent greeting to {celebrant['name']} ({celebrant['email']})")
    i = len(celebrants)
    print(f"Sent all greetings. ({i}/{i})")
