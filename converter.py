import requests
from exchange_rate_api import ExchangeRateAPI

class CurrencyConverter:
    def __init__(self):
        self.converter_api = ExchangeRateAPI()

    """verifies that the currency code entered is valid"""
    def valid_currency_check(self, currency):
        avail_curriencies = self.converter_api.get_avail_currencies()
        return currency in avail_curriencies        
    
    def convert_currency(self, from_currency, to_currency, amount):
        conversion_rate = self.converter_api.get_conversion_rate(from_currency, to_currency)
        converted_amount = amount * conversion_rate
        formatted_amount= self.converter_api.format_currency(converted_amount, to_currency)
        return formatted_amount


