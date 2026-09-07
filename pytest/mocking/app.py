import requests
import datetime

def get_usd_price():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data['rates']['IRR']

def is_morning():
    now = datetime.datetime.now()
    return now.hour < 12