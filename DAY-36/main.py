import requests
from datetime import date, timedelta
import html
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : "MDYWM3SU0J37L2MD"
}
url = "https://www.alphavantage.co/query"
account_sid = 'AC025e00e80850cff3eceb291b2836a60f'
auth_token = 'a8b4485d1b21af6b2c7efa3ced16be5c'
client = Client(account_sid, auth_token)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
output_data = requests.get(url=url, params=parameters)
stock_data = output_data.json()
date_yesterday = date.today() - timedelta(days=1)
date_day_before = date_yesterday - timedelta(days=1)
close_day_before = float(stock_data["Time Series (Daily)"][str(date_day_before)]["4. close"])
change = abs(float(stock_data["Time Series (Daily)"][str(date_yesterday)]["4. close"]) - float(stock_data["Time Series (Daily)"][str(date_day_before)]["4. close"]))
percent = (change / close_day_before) *100
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percent<5 :
    parameters_news = {
        "q" : COMPANY_NAME,
        "from" : str(date_day_before),
        "sortBy" : "publishedAt",
        "apikey" : "fb072de47870472b8bed413928e6fdc2"
    }
    output_news = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)
    news_data = output_news.json()['articles']
    for i in range(3):
        headline = html.unescape(news_data[i]["description"])
        content = html.unescape(news_data[i]["content"])
        my_message = f"TSLA: 🔺{percent}%\n" \
                     f"Headline: {headline}\n" \
                     f" Brief: {content} "

        message = client.messages.create(
            from_='+17165266244',
            body=my_message,
            to='+918248298176'
        )

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

