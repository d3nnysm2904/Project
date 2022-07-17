from crypt import methods
from distutils.log import error
from locale import currency
from random import randint, choice, sample
from flask import Flask, jsonify, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes


app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
c = CurrencyRates()
co = CurrencyCodes()
use_decimal = True

app.config['SECRET_KEY'] = "oh-so-secret"


@app.route('/')
def home_page():
    return render_template('home.html')


currency = {'EUR'
            'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}


@app.route('/', methods=['GET', 'POST'])
def home():

    currency_from = request.form['currency']
    currency_to = request.form['currency2']
    amount = request.form['amount']
    amount = int(amount)

    answer2 = 'Not valid '

    if amount != '' or currency_to != currency or currency_from != currency:
        amount = int(amount)

    else:
        amount = 2
        currency_from = None
        currency_to = None
        answer = None
        rate = None
        symbol = None
        flash('Invalid input')
        return render_template('home.html', answer2=answer2)

        # amount = False
        # currency_from = False
        # currency_to = False

    rate = c.convert(currency_from, currency_to, amount)
    symbol = co.get_symbol(currency_to)
    answer = f"The result is {symbol} {rate} "

    if rate is None or symbol is None:
        rate = False
        symbol = False

    return render_template('home.html', answer=answer, symbol=symbol)
