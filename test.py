import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Currency Converter', response.data)

    def test_conversion_route(self):
        response = self.app.post('/', data={'amount': 1, 'from_currency': 'USD', 'to_currency': 'USD'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Converted Amount:', response.data)


class ConversionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_conversion_calculation(self):
        response = self.app.post('/', data={'amount': 100, 'from_currency': 'USD', 'to_currency': 'EUR'})
        self.assertEqual(response.status_code, 200)

        # Assuming a known conversion rate of 1 USD = 0.85 EUR
        expected_conversion = 100 * 0.85

        # Extracting the converted amount from the response HTML
        converted_amount = float(response.data.decode('utf-8').split('Converted Amount: ')[1])

        # Asserting that the calculated converted amount matches the expected conversion
        self.assertAlmostEqual(converted_amount, expected_conversion, places=2)