
from twilio.rest import Client
import requests

api_key = "your API key for weather app"
account_sid = "Twilio account sid" #for twilio
auth_token = "twilio account authorization token" #for twilio
message = "Any message"

request = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=30.212942&lon=-93.218910&cnt=4&appid=cb2afbc18c170c7c998c003a20f3258b")
request.raise_for_status()

json_file = request.json()

will_it_rain = False

for i in json_file["list"]:
    condition = i["weather"][0]["id"]
    if int(condition) < 700:
        will_it_rain = True

if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="+1sender phone number",
        to="+1receiver phone number",
    )
    print(f"Message sent: {message}")



