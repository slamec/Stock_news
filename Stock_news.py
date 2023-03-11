import yfinance as yf 
import json

symbols = ['AAPL', 'GOOG', 'AMZN']

for symbol in symbols:
    ticker = yf.Ticker(symbol)
    ticker_news = ticker.news

    data_sorted = json.dumps(ticker_news, indent=4, sort_keys=True)

    news_dict = {}

    for items in ticker_news:
        related_ticker = items['relatedTickers']
        title = items['title']
        link = items['link']
        

        for ticker in related_ticker:
            if ticker not in news_dict:
                news_dict[ticker] = set()
            news_dict[ticker].add((title, link))

    count = 0

    for title, link in news_dict.get(symbol, []):
        print(symbol)
        print(title)
        print(link)
        count += 1
        if count == 3:
            break

    print('\n')




