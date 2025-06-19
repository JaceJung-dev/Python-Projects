import datetime as dt
import os
import pandas as pd
import random
import smtplib
from collections import defaultdict

MY_NAME = "your name"
MY_EMAIL = "example@gmail.com"
PASSWORD = "xxxx xxxx xxxx xxxx"
BASEDIR = os.path.dirname(__file__)

# 1. Create and save a CSV file with your friends' birthday detail.
friends = {
    "name": [
        "friend1",
        "friend2",
        "friend3",
        "friend4",
    ],
    "email": [
        "friend1@gmail.com",
        "friend2@gmail.com",
        "friend3@gmail.com",
        "friend4@gmail.com",
    ],
    "year": [1993, 1980, 1974, 1952],
    "month": [6, 6, 11, 10],
    "day": [19, 19, 17, 1],
}

data = pd.DataFrame(friends)
data.to_csv(f"{BASEDIR}/birthdays.csv", index=False)

# 2. Get today's date.
now = dt.datetime.now()
today = (now.month, now.day)

# 3. Load the birthday data and organize it into a dictionary grouped by.
birthdays = pd.read_csv(f"{BASEDIR}/birthdays.csv")
birthdays_dict = defaultdict(list)

for _, data_row in birthdays.iterrows():
    key = (data_row["month"], data_row["day"])
    birthdays_dict[key].append(data_row)

# 4. If today matches any birthday, send a email to each person.
if today in birthdays_dict:
    birthday_people = birthdays_dict[today]
    for birthday_person in birthday_people:
        file_path = f"{BASEDIR}/letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(file_path, mode="r") as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
            contents = contents.replace("[YOUR_NAME]", MY_NAME)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}",
            )
