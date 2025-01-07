import os
import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv('EXCHANGE_API_KEY')
if not API_KEY:
    raise ValueError("API key not found in .env file or environment variables.")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    url = BASE_URL + from_currency
    response = requests.get(url)
    data = response.json()
    
    if data['result'] == 'success':
        rate = data['conversion_rates'].get(to_currency)
        if rate:
            return rate
        else:
            print(f"Currency {to_currency} not found in response.")
            return None
    else:
        print("Error:", data.get("error-type", "Unknown error"))
        return None

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        return amount * rate
    else:
        return None



from_currency = input("Enter the currecy you want to exchange from: ")
to_currency = input("Enter the currecy you want to exchange to: ")
amount = float(input("Enter the amount: "))

converted_amount = convert_currency(amount, from_currency, to_currency)
if converted_amount:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print("Conversion failed.")
