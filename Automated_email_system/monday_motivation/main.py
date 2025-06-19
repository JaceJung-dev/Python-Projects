import datetime as dt
import os
import random
import smtplib

MY_EMAIL = "yourmail@gmail.com"
PASSWORD = "xxxx xxxx xxxx xxxx"
BASEDIR = os.path.dirname(__file__)
TO_EMAIL = ["example@gmail.com", "example2@gmail.com"]

all_quotes = []
quote = ""

# Weekday
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open(f"{BASEDIR}/quotes.txt", mode="r") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )
