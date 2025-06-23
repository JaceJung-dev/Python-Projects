import datetime as dt
import requests
import smtplib
import time

MY_EMAIL = "example@gmail.com"
PASSWORD = "xxxx xxxx xxxx xxxx"
MY_LAT = 37.566536
MY_LONG = 126.9779668
ISS_URL = "http://api.open-notify.org/iss-now.json"
SUNSET_SUNRISE_URL = "https://api.sunrise-sunset.org/json"


def is_iss_overhead():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url=SUNSET_SUNRISE_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="example2@gmail.com",
                msg="Subject:LOOK UP👆\n\nThe ISS is above you in the sky!",
            )
