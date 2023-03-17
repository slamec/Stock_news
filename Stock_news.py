import yfinance as yf 
import json #to check json file
import csv

portfolio = 'Portfolio.csv'

def read_csv(file_name):
    """Function reads tickers from a csv Yahoo.com file"""
    
    symbols = set()

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            symbols.add(row[0])

    return list(symbols)

symbols = read_csv(portfolio)

#print(symbols)

import yfinance as yf

def ticker_news(stock_name):
    """This function accepts n number of ticker symbols and returns 3 top news for each."""
    
    #news string
    news_string = " "

    # Get news for each ticker
    for symbol in stock_name:
        ticker = yf.Ticker(symbol)
        ticker_news = ticker.news
        
        # New dictionary
        news_dict = {}
        
        # Keep track of news items that have already been added
        added_news = set()
        
        # Loop through yf dictionary
        for items in ticker_news:
            try:
                related_ticker = items['relatedTickers']
            except KeyError:
                related_ticker = []
            title = items['title']
            link = items['link']
            
            # Avoid duplicates
            if (title, link) not in added_news:
                for ticker in related_ticker:
                    if ticker not in news_dict:
                        news_dict[ticker] = set()
                    news_dict[ticker].add((title, link))
                added_news.add((title, link))
        
        count = 0
        
        # Write news to a string
        for title, link in news_dict.get(symbol, []):
            news_string += f"<br><br>{'$'}{symbol}{':'}\n"
            news_string += f'<a href=\"{link}\">{title}</a>\n'
            count += 1
            if count == 3:
                break
        
    return news_string

# print(ticker_news(symbols))

with open('news_test.html', 'w') as file:
    file.write(ticker_news(symbols)) 