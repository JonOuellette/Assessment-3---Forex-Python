import requests

class CurrencyExchange:
    def __init__(self):
        self.converter_api = ExchangeRateAPI()

    """verifies that the currency code entered is valid"""
    def valid_currency_check(self, currency):
        avail_curriencies = self.converter_api.get_avail_currencies()
        return currency in avail_curriencies        
    
    def convert_currency(self, from_currency, to_currency, amount):
        conversion_rate = self.converter_api.get_conversion_rate(from_currency, to_currency)
        converted_amount = amount * conversion_rate
        return self.converter_api.format_currency(converted_amount, to_currency)


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
    
    """retrieves the currency symbols data from the API and appends the to currency symbol to the amount and sets the currency value to 2 decimal places"""
    def format_currency(self, amount, currency):
        response = requests.get(f'{self.base_url}/symbols')
        data = response.json()
        symbol = data['symbols'][currency]['symbol']
        return f'{symbol} {amount:.2f}'