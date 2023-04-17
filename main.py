import requests
from twilio.rest import Client
#import smtplib

##### UPDATE THESE #####
NEWS_API_KEY = ""
ALPHA_VANTAGE_API_KEY = ""
TWILIO_API_KEY = ""
TWILIO_ACCOUNT_SID = ""
FROM_PHONE_NUMBER = ""
TO_PHONE_NUMBER = ""
##### UPDATE THESE #####

# Update these if you want to follow a different stock
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# For API calls
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# Get change of stock price for the past 2 days
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": ALPHA_VANTAGE_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# Get yesterdays closing data
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
#print(yesterday_closing_price)

# Get day before yesterdays closing data
ereyesterday_data = stock_data_list[1]
ereyesterday_closing_data = ereyesterday_data["4. close"]
#print(ereyesterday_closing_data)

# Find difference
difference = abs(float(yesterday_closing_price) - float(ereyesterday_closing_data))
#print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
#print(diff_percent)

# If Stock change is greater than 5 percent then get news and send a SMS
if diff_percent >= 0:
    # Get news
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]

    # Format message to be sent
    if difference >= 0:
        header = f"{STOCK}: 🔺{round(difference,2)}%\n"
    else:
        header = f"{STOCK}: 🔻{round(difference,2)}%\n"

    body = ""
    for news_article in news_data:
        body += f"Headline: {news_article['title']}\nBrief: {news_article['description']}\n"
    body = body.strip()
    #print(body)

    # Send out SMS message
    message = header + body
    #print(message)
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_API_KEY)
    stock_update = client.messages.create(body=message, from=FROM_PHONE_NUMBER, to=TO_PHONE_NUMBER)

    # Send out an Email instead!
    # Comment out the commands above that send a SMS message
    # Uncomment the `import smtplib` at the top of this file
    # Un-Comment the commands below -
    # and update the information below for your account
    # my_email = ""
    # to_email = ""
    # password = ""
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs=to_email,
    #         msg=f"{header}\n\n{body}"
    #     )
