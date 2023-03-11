import yfinance as yf 
import json


ticker = yf.Ticker('AAPL')
ticker_news = ticker.news

data_sorted = json.dumps(ticker_news, indent=4, sort_keys=True)

# print(data_sorted)

with open('test_data.txt', 'w') as file:
    file.writelines(data_sorted)