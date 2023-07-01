import requests

class CurrencyExchange:
    def __init__(self):
        self.converter_api = ExchangeRateAPI()
            
    



class ExchangeRateAPI:
    def __init__(self):
        self.base_url = 'https://api.exchangerate.host'

    """retrieves the available curriencies and their currency codes"""
    def get_avail_currencies(self):
        response = requests.get(f'{self.base_url}/symbols')
        data = response.json()
        # print(data)
        return list(data['symbols'].keys())
    
    """retrieves the conversion rates for the two curriences provided by the user"""
    def get_conversion_rate(self, from_currency, to_currency):
        response = requests.get(f'{self.base_url}/convert?from={from_currency}&to={to_currency}')
        data = response.json()
        return data['info'][to_currency]['rate']
    
    """retrieves the currency symbols data from the API"""
    def format_currency(self, amount, currency):
        response = requests.get(f'{self.base_url}/symbols')
        data = response.json()
        symbol = data['symbols'][currency]['symbol']
        return f'{symbol} {amount:.2f}'