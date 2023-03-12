import yfinance as yf 
import json

symbols = ['AAPL', 'GOOG', 'AMZN']

def ticker_news(stock_name):
    """This function accepts n number of ticker symbols and returns 3 top news for each."""

    #get news for ticker
    for symbol in stock_name:
        ticker = yf.Ticker(symbol)
        ticker_news = ticker.news

        # data_sorted = json.dumps(ticker_news, indent=4, sort_keys=True)
        
        #new dictionary 
        news_dict = {}

        #loop through yf dictionary
        for items in ticker_news:
            related_ticker = items['relatedTickers']
            title = items['title']
            link = items['link']
            
            #avoid duplicates
            for ticker in related_ticker:
                if ticker not in news_dict:
                    news_dict[ticker] = set()
                else:
                    news_dict[ticker].add((title, link))

        count = 0

        #print news from python 
        for title, link in news_dict.get(symbol, []):
            print(symbol)
            print(title)
            print(link)
            count += 1
            if count == 3:
                break

        print('\n')

ticker_news(symbols)




