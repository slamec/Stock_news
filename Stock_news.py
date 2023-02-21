import requests 
import json

with open('API_key.txt') as key:
    api_key = key.read()

url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=PG&sort=LATEST&limit=5&apikey=api_key'
r = requests.get(url)
data = r.json()

sorted_data = (json.dumps(data, indent=4, sort_keys=True))


with open('dict.txt', 'w') as file:
    file.writelines(sorted_data)

with open('test_data.txt', 'w') as file:

    for items in data['feed']:
        for ticker in items['ticker_sentiment']:
            tickers = (ticker['ticker'])
        summary = items['summary']
        links = items['url']
    
        
        file.write(str(tickers) + ':' + '\n' + str(summary) + '\n' + str(links) + '\n')


