import yfinance as yf
import pandas_ta as ta
import requests
import time

TOKEN = "8766852110:AAEVE4T-hWXO_QWAhuHe3nJO1H7Xk8F2a2c"
CHAT_ID = "7496717018"

symbols = [
"AKBNK.IS","ALARK.IS","ARCLK.IS","ASELS.IS","ASTOR.IS","BIMAS.IS",
"EKGYO.IS","ENKAI.IS","EREGL.IS","FROTO.IS","GARAN.IS","GUBRF.IS",
"HEKTS.IS","ISCTR.IS","KCHOL.IS","KONTR.IS","KOZAA.IS","KOZAL.IS",
"KRDMD.IS","MGROS.IS","ODAS.IS","OYAKC.IS","PETKM.IS","SAHOL.IS",
"SASA.IS","SISE.IS","TCELL.IS","THYAO.IS","TOASO.IS","TUPRS.IS",
"VESTL.IS","YKBNK.IS"
]

last_signal = {}

def send(msg):
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

send("Bot çalıştı ve tarama başladı")

while True:
for symbol in symbols:
try:
data15 = yf.download(symbol, period="5d", interval="15m")
data1h = yf.download(symbol, period="1mo", interval="1h")

ema50 = ta.ema(data1h["Close"], length=50).iloc[-1]
price = data1h["Close"].iloc[-1]

st = ta.supertrend(
high=data15["High"],
low=data15["Low"],
close=data15["Close"],
length=10,
multiplier=3
)

prev = st["SUPERTd_10_3.0"].iloc[-2]
now = st["SUPERTd_10_3.0"].iloc[-1]

name = symbol.replace(".IS", "")

if price > ema50 and prev == -1 and now == 1:
if last_signal.get(symbol) != "BUY":
send(f"BUY - {name}\nEMA50 üstünde\n15dk SuperTrend AL verdi")
last_signal[symbol] = "BUY"

if price < ema50 and prev == 1 and now == -1:
if last_signal.get(symbol) != "SELL":
send(f"SELL - {name}\nEMA50 altında\n15dk SuperTrend SAT verdi")
last_signal[symbol] = "SELL"

except Exception as e:
send(f"HATA {symbol}: {e}")

time.sleep(300)
