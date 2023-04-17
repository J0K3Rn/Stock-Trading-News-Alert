# Stock-Trading-News-Alert
 
A stock following program that sends a SMS alert and relevant news

Features:
- Follows a stock and calculates the change in that stock
- Gathers relevant news data
- Sends out a SMS if stock threshold changes by a particular amount
- Can easily be changed for other stocks
- Can easily switch to SMTP mail if SMS is deemed unworthy (See bottom of `main.py`)

How to run:
- Download repository
- Create an account on ![Twilio](https://www.twilio.com/), get your api key, account sid, phone numbers, and update `main.py`
- Create an account on ![Alpha Vantage](https://www.alphavantage.co/), get your api key and update `main.py`
- Create an account on ![News API](https://newsapi.org/), get your api key and update `main.py`
- Open downloaded repository with a command line interface
- run `pip install twilio`
- run `python main.py`
- Script will be run and message will be sent if stock change meets threshold.
- Update the threshold and company by editing `main.py`

Stock Message Example:

![alt text](https://github.com/J0K3Rn/Stock-Trading-News-Alert/blob/main/screenshots/stock_message.png?raw=true) 
