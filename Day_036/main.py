import json
from email.mime.text import MIMEText
from operator import index

import requests
from datetime import datetime as dt
from datetime import timedelta as td
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "your api key"
API_KEY_NEWS = "your api new key"


with open("data.json", "r") as reader:
    data = json.load(reader)
refresh_date_today = data["Meta Data"]["3. Last Refreshed"]
refresh_date_past_day = (dt.strptime(refresh_date_today, "%Y-%m-%d") - td(days=1)).strftime("%Y-%m-%d")
close_amt = data["Time Series (Daily)"][refresh_date_today]["4. close"]
past_day_close_amt = data["Time Series (Daily)"][refresh_date_past_day]["4. close"]
get_remainder = eval(f"{(float(close_amt) - float(past_day_close_amt)) / float(past_day_close_amt) * 100} ")
stk_high = data["Time Series (Daily)"][refresh_date_today]["2. high"]
stk_low = data["Time Series (Daily)"][refresh_date_past_day]["3. low"]
# reach API connection limit had to make it local
# refresh_date_today = tsla_stock.json()["Meta Data"]["3. Last Refreshed"]
# add back after api is back to close amt both tsla_stock.json()['Time Series (Daily)']


tsla_news = requests.get(url="https://newsapi.org/v2/everything?q=tesla&from={}&sortBy=publishedAt&apiKey={}".format(refresh_date_today, API_KEY_NEWS))
tsla_news.raise_for_status()
with open("tsla_news_data.json", "r") as reader:
    tsla_news_data = json.load(reader)
tsla_news_json = tsla_news.json()
with open("tsla_news_data.json", "w", encoding="utf-8") as writer:
    json.dump(tsla_news_json, writer, indent=4, ensure_ascii=False)

index_ = 0
clean_data = ["source", "publishedAt"]
new_articles = [index_ + i for i, _ in enumerate(tsla_news_data["articles"])]
today_news = [f"{tsla_news_data["articles"][0][str(news_data)]}\n" for news_data in tsla_news_data["articles"][0] if news_data not in clean_data]
yesterdays_new = [f"{tsla_news_data["articles"][1][str(news_data)]}\n" for news_data in tsla_news_data["articles"][1] if news_data not in clean_data]
date_time = tsla_news_json["articles"]
tsla_recent_news = f"{date_time[0]["publishedAt"]}:\n{''.join(map(str,today_news))} \n{date_time[0]["publishedAt"]}:\n{''.join(map(str,yesterdays_new))}"

tsla_stock = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(STOCK, API_KEY))
tsla_stock.raise_for_status()


smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "your_email@gmail.com"
smtp_password = "password"

from_addr = smtp_username
to_addr = "send_to@email.com"
subject = "TSLA: STOCK updates"
body = f"TSLA stocks: \n{get_remainder:.2f}%\nHIGH: {stk_high}\nLOW: {stk_low}\n" + f"{tsla_recent_news}"
msg = MIMEText(body, 'plain', 'utf-8')

try:
    with smtplib.SMTP(smtp_server, smtp_port) as mail_man:
        mail_man.starttls()
        mail_man.login(smtp_username, smtp_password)

        mail_man.sendmail(from_addr, to_addr, msg.as_string())
except Exception as e:
    print(f"Oops... : {e}")
else:
    print("E-Mail has been sent!")


