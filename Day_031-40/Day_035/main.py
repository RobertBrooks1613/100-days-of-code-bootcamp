import requests
import json

from twilio.rest import Client

import weather_data_dict
import twilio

my_lat = ""
my_lng = ""
my_api_key = ""


weather_params = {
    "lat": "",
    "lon": "",
    "cnt": 4,
    "appid": my_api_key,
}
def local_current_forcast():
    global weather_params
    my_local_weather = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?", params=weather_params)
    my_local_weather.raise_for_status()
    print(my_local_weather.json()["main"])

def _5_day_3_hr_forcast():
    my_sms_key =""
    my_acct_sid = ""
    my_auth_token = ""
    from datetime import datetime as dt
    from datetime import timedelta as td
    global weather_params
    my_5day_3hr_weather = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?", params=weather_params)
    my_5day_3hr_weather.raise_for_status()

    weather_json = my_5day_3hr_weather.json()["list"]
    weather_ids = [weather_json[i]["weather"][0]["id"] for i, _ in enumerate(weather_json)]
    weather_dt = [(dt.fromtimestamp(weather_json[i]["dt"]) - td(hours=5)).strftime("%m-%d-%Y, %H:%M:%S") for i, _ in enumerate(weather_json)]
    # data_forcast = [print(f"weather is {weather_data_dict.weather_dict[i]} Think ahead!") for i in weather_ids if i > 700]
    for i, id_ in enumerate(weather_ids):
        if id_ > 700:
            client = Client(my_acct_sid, my_auth_token)
            message = client.messages \
                .create(
                body=f"Bob Weather Forcast\nWeather time stamp: {weather_dt[i]}\n"
                     f"weather is {weather_data_dict.weather_dict[id_]} Think ahead!",
                from_= "+",
                to= "+"
            )
            print(message.status)


_5_day_3_hr_forcast()