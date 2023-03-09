import requests
import datetime as dt
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

STOCK_API_KEY = "2T4ORMGCIYG0A1A8"
NEW_API_KEY = "e2b5d887648d4c30a6a230faa30ba4ec"

stock_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK_NAME,
    'interval': '60min',
    'apikey': STOCK_API_KEY,
}
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday = dt.datetime.today() - dt.timedelta(days=1)
day_before_yesterday = dt.datetime.today() - dt.timedelta(days=2)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()
print(data['Time Series (60min)'])
stock_data = [value for (key, value) in data['Time Series (60min)'].items()]

opening_price = float(stock_data[-1]['1. open'])
closing_price = float(stock_data[0]['4. close'])

print(opening_price, closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(opening_price - closing_price)
print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_difference = (difference / opening_price)*100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
news_params = {
    'apiKey': NEW_API_KEY,
    'country':'us',
    'q': COMPANY_NAME,
    # 'sources': '/v2/top-headlines/sources',
}

news_response = requests.get(url=NEWS_ENDPOINT)
news_response.raise_for_status()
print(news_response.json())
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

