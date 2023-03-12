import yfinance as yf 
import json #to check json file
import csv

portfolio = 'Portfolio.csv'

def read_csv(file_name):
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

def ticker_news(stock_name, output_file):
    """This function accepts n number of ticker symbols and returns 3 top news for each."""
    
    # Open the file for writing
    with open(output_file, 'w') as f:
    
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
            
            # Write news to file
            for title, link in news_dict.get(symbol, []):
                f.write(f"{symbol}\n")
                f.write(f"{title}\n")
                f.write(f"{link}\n")
                count += 1
                if count == 3:
                    break
            
            f.write('\n')

output_file = 'news_test.txt'

ticker_news(symbols, output_file)