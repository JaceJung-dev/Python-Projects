# Automated Email System (SMTP)

## What I learned
- How to use Automated Email System with SMTP (Simple Mail Transfer Protocol).
- How to manage dates and time with `datetime` module.
- Gained experience using `defaultdict` from `collections` module ot organize data efficiently.

## What I did
- Implemented automated Monday motivation email send every week.
- Developed a feature to send birthday wishes to friends automatically via email.

## Code Example in Action

### SMTP
SMTP is a communication protocol used to send emails over the Internet. It defines how email messages are transmitted between servers and from email clients to servers.

`smtplib` is a built-in Python library that provides tools for sending emails using the SMTP protocol.

```python
import smtplib

MY_EMAIL = "example@gmail.com"
TO_EMIAL = "friend@gmail.com
PASSWORD = "xxxx xxxx xxxx xxxx"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="friend@gmail.com",
                        msg="Subject:Title\n\nThis is the body of my email.")
```

### `datetime`
```python
import datetime as dt

now = dt.datetime.now()
print(now)  # 2025-06-19 12:34:56.789123

year = now.year
month = now.month
print(year, month)  # 2025 6

day_of_week = now.weekday()
print(day_of_week)  # 3

date_of_birth = dt.datetime(year=1982, month=12, day=25)
print(date_of_birth)  # 1982-12-25 00:00:00
```

### `defaultdict`
defaultdict is a subclass of the built-in Python dict that automatically assigns a default value to a key that doesn’t exist yet.

```python
from collections import defaultdict

# Automatically sets an empty list as the default value.
my_dict = defaultdict(list)

my_dict["a"].append(1)
my_dict["a"].append(2)
my_dict["b"].append(3)

print(my_dict)  # {'a': [1, 2], 'b': [3]}
```