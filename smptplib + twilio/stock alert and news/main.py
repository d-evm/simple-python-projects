import requests
from twilio.rest import Client

account_sid = YOUR_ACC_SID
auth_token = YOUR_AUTH_TOKEN

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "XEXUHIMVILRVOP1S"
NEWS_API_KEY = "25e859278dee42d3b05f807d12239c56"

def get_news():
    news_endpoint = "https://newsapi.org/v2/top-headlines?"
    news_parameters = {
        "q": STOCK,
        "apikey": NEWS_API_KEY
    }

    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    print(news_data)
    print(type(news_data))
    headline = news_data['articles'][0]['title']
    description = news_data['articles'][0]['description']

    return [headline, description]

def send_alert(change):
    news = get_news()

    headline = news[0]
    brief = news[1]

    symbol = "🔺" if change > 0 else "🔻"

    body_text = f""" 
ALERT!

{STOCK}: {symbol}{change}%

Headline: {headline}

Brief: {brief}

    """

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=YOUR_TWILIO_NUMBER,
        body=body_text,
        to=RECEIVER_NUMBER
    )

def get_change_percent():
    stock_endpoint = "https://www.alphavantage.co/query?"
    stock_parameters = {
        "function": "GLOBAL_QUOTE",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }

    stock_response = requests.get(url=stock_endpoint, params=stock_parameters)
    stock_response.raise_for_status()

    stock_data = stock_response.json()

    change = float((stock_data["Global Quote"]["10. change percent"])[:-1])

    if change >= 10 or change <= -10:
        send_alert(change)


get_change_percent()

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
