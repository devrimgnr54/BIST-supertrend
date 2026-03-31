import yfinance as yf
import pandas_ta as ta
import requests
import time

TOKEN = "8766852110:AAEVE4T-hWXO_QWAhuHe3nJO1H7Xk8F2a2c"
CHAT_ID = "7496717018"

import reques

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
url,
data={
"chat_id": CHAT_ID,
"text": "Bot çalıştı"
}
)
