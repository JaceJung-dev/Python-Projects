import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OWM_API_KEY = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

MY_LAT = 37.566536
MY_LONG = 126.977966

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages.create(
        body="It's going to rain today, Remember to brain an Umbrella☔️",
        from_="Twilio phone number",
        to="Your verified number",
    )
else:
    message = client.messages.create(
        body="No rain today, leave the umbrella at home!☀️",
        from_="Twilio phone number",
        to="Your verified number",
    )
