# Stock News Tracker

This script tracks the daily changes in the stock price of a specified company and sends an SMS notification if the stock price changes by 5% or more from the previous day. The notification includes the latest news articles related to the company.

## How It Works

1. **Stock Price Tracking**: The script fetches the daily stock price data for the specified company from the Alpha Vantage API, calculating the percentage change from the previous day's closing price.
2. **News Fetching**: If the percentage change is equal to or greater than 5%, the script then fetches the top three news articles related to the company from the News API.
3. **SMS Notification**: The selected news articles, along with the stock price change, are sent via SMS using the Twilio service. The messages include a visual indicator ("🔺" for a price increase, "🔻" for a price decrease) along with the percentage change, headline, and URL for each news article.

## Requirements

- An Alpha Vantage API key for fetching stock price data.
- A News API key for fetching news articles.
- Twilio account credentials (account SID and auth token) for sending SMS notifications.

## Configuration

The script requires the following variables to be set:

- `STOCK`: The stock symbol of the company you want to track (e.g., "TSLA" for Tesla Inc).
- `COMPANY_NAME`: The name of the company you want to track (e.g., "Tesla Inc").
- `STOCK_API_KEY`: Your Alpha Vantage API key.
- `NEWS_API_KEY`: Your News API key.
- Twilio `account_sid` and `auth_token`: Your Twilio credentials.
- Twilio phone numbers for `from_` and `to`: The sender and recipient phone numbers for SMS notifications.

## Usage

Simply update the `STOCK` and `COMPANY_NAME` variables with the desired stock symbol and company name, then run the script. It will check the stock price change for the specified company, and if the change is 5% or more, it will send an SMS notification with the latest news articles.

---

Please replace the placeholder values in the script with your actual API keys, stock symbol, company name, and Twilio credentials before running the code. Feel free to modify the README to suit your specific needs or provide additional information on setup and usage.
