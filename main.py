import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "APIKEY"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response_stock = requests.get(STOCK_ENDPOINT, stock_params)
response_stock.raise_for_status()


TSLA_stock_data = response_stock.json()
TSLA_time_series = TSLA_stock_data["Time Series (Daily)"]
dates = sorted(TSLA_time_series.keys(), reverse=True)

TSLA_yesterday_close = float(TSLA_time_series[dates[0]]["4. close"])
TSLA_day_before_close = float(TSLA_time_series[dates[1]]["4. close"])

change_percent = round(((TSLA_yesterday_close - TSLA_day_before_close) / TSLA_day_before_close) * 100)

up_down = None

if change_percent > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


if abs(change_percent) >= 5:
    NEWS_API_KEY = "NEWS_API_KEY_HERE"

    news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME
    }

    response_news = requests.get(NEWS_ENDPOINT, news_params)
    articles = response_news.json()["articles"]
    three_articles = articles[:3]

    formatted_articles =[f"{STOCK}: {up_down}{change_percent}%\nHeadline: {article['title']}. \nURL: {article['url']}" for article in three_articles]


#Twilio section # add your phone tokens and phone numbers

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

for article in formatted_articles:
    message = client.messages.create(
         body=article,
         from_='+44',
         to='+44'
    )
