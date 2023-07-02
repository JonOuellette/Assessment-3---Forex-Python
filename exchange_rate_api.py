import requests

class ExchangeRateAPI:
    def __init__(self):
        self.base_url = 'https://api.exchangerate.host'
        
    # retrieves the available curriencies and their currency codes
    def get_avail_currencies(self):
        response = requests.get(f'{self.base_url}/symbols')
        data = response.json()
        # print(data)
        return data.get('symbols', {})
    
    """retrieves the conversion rates for the two curriences provided by the user"""
    def get_conversion_rate(self, from_currency, to_currency):
        response = requests.get(f'{self.base_url}/convert?from={from_currency}&to={to_currency}')
        data = response.json()
        # print(data)
        return data['info']['rate']
    
    """retrieves the currency symbols data from the API and appends the to currency symbol to the amount and sets the currency value to 2 decimal places"""
    def format_currency(self, amount, currency):
        response = requests.get(f'{self.base_url}/symbols')
        data = response.json()
        symbols = data.get('symbols', {})
        symbol = symbols.get(currency, {}).get('symbol', '')
        return f'{symbol} {amount:.2f}'


