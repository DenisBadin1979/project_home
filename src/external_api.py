import requests
import os
from dotenv import load_dotenv

load_dotenv()
def currency_converter(currency: str, amount: str) -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": amount,
        "from": currency,
        "to": "RUB"}
    api_key_d = os.getenv('API_KEY')
    headers = {"apikey": api_key_d}
    response = requests.get(url, headers=headers, params=payload)
    result_convert = response.json()
    return result_convert['result']







