import requests

class CurrencyExchange:
    def __init__(self):
        self.converter_api = ExchangeRateAPI()
            
    response = requests.get('https://api.exchangerate.host/symbols')
    data = response.json



class ExchangeRateAPI:
    def __init__(self):
        self.base_url = 'https://api.exchangerate.host'