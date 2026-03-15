#!/usr/bin/env python3

import requests
import json
import os

city = input("Enter name of city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=9ec246f4959546a3936143122261103&q={city}"

r = requests.get(url)

weatherDictionary = json.loads(r.text)

print(weatherDictionary)

currentTemp = weatherDictionary["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {currentTemp} degrees'")