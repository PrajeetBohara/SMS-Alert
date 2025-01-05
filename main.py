#website used openweathermap.org to use api keys
#apikey = cb2afbc18c170c7c998c003a20f3258b

import requests

api_key = "cb2afbc18c170c7c998c003a20f3258b"

request = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=30.212942&lon=-93.218910&cnt=4&appid=cb2afbc18c170c7c998c003a20f3258b")
request.raise_for_status()

json_file = request.json()

will_it_rain = False

for i in json_file["list"]:
    condition = i["weather"][0]["id"]
    if int(condition) < 700:
        will_it_rain = True

if will_it_rain:
    print("Bring an Umbrella")

#MQK5T4EK43BY49F2AUUPT626