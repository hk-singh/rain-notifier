import os

import requests
from datetime import datetime
from twilio.rest import Client

API_KEY = os.environ.get("API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

client = Client(account_sid, auth_token)

def rain_check(weather_code):
    if weather_code < 700:
        return True

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

MY_COORD = [51.642368, -1.311661]

weather_params = {
        "lat": MY_COORD[0],
        "lon": MY_COORD[1],
        "appid": API_KEY,
        "exclude": "current,minutely,daily"

    }

om_response = requests.get(url=OWM_ENDPOINT, params=weather_params)
om_response.raise_for_status()
weather_data = om_response.json()["hourly"][:12]
for i in range(0, len(weather_data)):
    if rain_check(weather_data[i]["weather"][0]["id"]):
        message = client.messages.create(
          from_='+447723343826',
          body='It is going to rain today, take your umbrella ☔️',
          to='+447925119022'
        )
        print(message.sid)
