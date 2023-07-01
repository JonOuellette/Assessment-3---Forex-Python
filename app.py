from flask import Flask, request, render_template, jsonify 
from converter import CurrencyExchange

app = Flask(__name__)

converter = CurrencyExchange()

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    

    
    """Checks for POST request - if it is a POST request it then retrieves the user values for currency codes and amounts"""
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to currency']
        amount = request.form['amount']
    
        """Verifies if the currency codes entered are valid"""
        if not converter.is_valid_currency(from_currency) or not converter.is_valid_currency(to_currency):
            error_msg = "Invalid currency code."
            return render_template('home.html', error = error_msg)

        """Checks if the amount is a valid number and if not throws an error"""
        try:
            amount = float(amount)
    
        except ValueError:
            error_msg = "Invalid amount"
            return render_template("home.html", error = error_msg)

        
        """calls on the convert_currency function from the converter file and sets the converted currency to the variable converted_amount"""
        converted_amount = converter.convert_currency(from_currency, to_currency,amount)

        return render_template("home.html", converted_amount=converted_amount)

    return render_template("home.html")