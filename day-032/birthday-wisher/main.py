import datetime as dt
import pandas as pd
import random
import smtplib

"""
Sends a birthday greeting to a celebrant if it's their birthday today.
The program takes a random template from letter_templates/

"""
MY_EMAIL = "MY_EMAIL"
APP_PASSWORD = "MY_PASS"

now = dt.datetime.now()
# Today's month and day
now_md = (now.month, now.day)

birthdays_df = pd.read_csv("birthdays.csv")
birthdays = {}
celebrants = []

# Create a dict for birthdays. (Redundant, but still getting the hang of pandas)
for row in birthdays_df.iterrows():
    name = row[1][0]
    month = row[1][3]
    day = row[1][4]
    email = row[1][1]
    birthdays[name] = (month, day, email)

for data in birthdays.items():
    name = data[0]
    birthdate = data[1][0:2]
    email = data[1][2]

    if now_md == birthdate:
        celebrants.append(name)

# Check if anyone is having their birthday today.
# "if celebrants" is shorter, but this is arguably more readable.
if len(celebrants) > 0:

    # Send greetings for each celbrant
    for celebrant in celebrants:
        template_path = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"
        with open(template_path) as f:
            template = f.read()
            birthday_message = template.replace("[NAME]", celebrant)

        message = f"Subject:Happy Birthday!\n\n{birthday_message}"
        celebrant_email = birthdays[celebrant][2]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs=celebrant_email, msg=birthday_message
            )
            print(f"Sent greeting to {celebrant} ({celebrant_email})")
