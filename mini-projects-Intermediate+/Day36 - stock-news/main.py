from datetime import datetime, timedelta
import os

import requests
from dotenv import load_dotenv

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Load environment variables
load_dotenv()
APIKEY = os.getenv('APIKEY')
NEWSAPIKEY = os.getenv('NEWSAPIKEY')


def get_day_closing_price(stock_data: dict, date_str: str) -> float:
    """Returns the closing stock price for a specific date."""
    return float(stock_data['Time Series (Daily)'][date_str]['4. close'])


def get_past_date(days_ago: int) -> str:
    """Returns the date from a given number of days ago, formatted as 'YYYY-MM-DD'."""
    today = datetime.now()
    past_date = today - timedelta(days=days_ago)
    return past_date.strftime("%Y-%m-%d")


# Fetch stock data from Alpha Vantage
api_url = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={APIKEY}"
response = requests.get(api_url)
stock_data = response.json()

# Get and print closing prices
closing_price_1 = get_day_closing_price(stock_data, get_past_date(days_ago=1))
print(f"Yesterday's closing price for {COMPANY_NAME} ({STOCK_NAME}): ${closing_price_1}")

closing_price_2 = get_day_closing_price(stock_data, get_past_date(days_ago=2))
print(f"Day before yesterday's closing price for {COMPANY_NAME} ({STOCK_NAME}): ${closing_price_2}")

# Find positive difference
positive_difference = round(abs(closing_price_2 - closing_price_1), 2)
print(f"Positive difference between the two days: ${positive_difference}")

# find percentage difference
percentage_difference = (positive_difference / closing_price_2) * 100
print(f"Percentage difference between the two days: {round(percentage_difference, 2)}%")


def get_company_news(company_name: str, api_key: str):
    parameters = {
        "q": company_name,
        "sortBy": "publishedAt",
        "apiKey": api_key,
        "pageSize": 3
    }
    response = requests.get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    articles = response.json().get("articles", [])

    for idx, article in enumerate(articles, start=1):
        print(f"\nArticle {idx}:")
        print(f"Headline: {article.get('title')}")
        print(f"Description: {article.get('description')}")
        print(f"URL: {article.get('url')}\n")


if percentage_difference > 5:
    print("Get News:")
    get_company_news(COMPANY_NAME,NEWSAPIKEY)

