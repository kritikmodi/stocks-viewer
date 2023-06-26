from flask import Flask, request
import yfinance as finance

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    company_code = request.form['text']
    company_ticker = finance.Ticker(company_code)
    return company_ticker

if __name__ == '__main__':
    app.run()
