import yfinance as yf 
import json

symbol = 'AAPL'

ticker = yf.Ticker(symbol)
ticker_news = ticker.news

data_sorted = json.dumps(ticker_news, indent=4, sort_keys=True)

news_dict = {}

for items in ticker_news:

    related_ticker = items['relatedTickers']
    link = items['link']
    title = items['title']

    for ticker in related_ticker:
        if ticker not in news_dict:
            news_dict[ticker] = set()
        else:
            news_dict[ticker].add((title, link))

for title, link in news_dict.get(symbol, []):
    print(symbol)
    print(title)
    print(link)




