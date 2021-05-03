import requests
from twilio.rest import Client
api_key = "enter_your_api_key"
account_sid = "enter_your_account_sid"
auth_token = "7enter_your_auth_token"
parameters = {"lat": -6.917464,
              "lon": 107.619125,
              "appid": api_key,
              "exclude": "currently,minutely,daily"}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data = response.json()
twell_hour_slice = data["hourly"][:12]
will_rain = False
for hour_data in twell_hour_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today, so bring an ☂️",
        from_='+16179348683',
        to='+919057992942'
    )
    print(message.status)