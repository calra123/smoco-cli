import yfinance as yf
import pandas as pd

# codes =  "INFY.NS RELIANCE.NS TCS.NS HDFCBANK.NS HINDUNILVR.NS ICICIBANK.NS HDFC.NS SBIN.NS BAJFINANCE.NS BHARTIARTL.NS KOTAKBANK.NS HCLTECH.NS WIPRO.NS ASIANPAINT.NS ITC.NS MARUTI.NS BAJAJFINSV.NS LT.NS AXISBANK.NS TITAN.NS ONGC.NS SUNPHARMA.NS ULTRACEMCO.NS NESTLEIND.NS TATAMOTORS.NS ADANIPORTS.NS JSWSTEEL.NS TATASTEEL.NS POWERGRID.NS TECHM.NS NTPC.NS HINDALCO.NS HDFCLIFE.NS DIVISLAB.NS IOC.NS SBILIFE.NS GRASIM.NS BAJAJ-AUTO.NS COALINDIA.NS M&M.NS SHREECEM.NS BRITANNIA.NS CIPLA.NS BHEL.NS EICHERMOT.NS INDUSINDBK.NS DRREDDY.NS GAIL.NS HEROMOTOCO.NS UPL.NS"
# codes = "RELIANCE.NS"

# codes = "^NSEI"
codes = "^NSEBANK"

data = yf.download(codes, period="10y",
	interval="1mo",
	group_by="ticker",
	auto_adjust=False)

# infy = yf.Ticker("INFY.NS")

# # get stock info
# infy.info

# # get historical market data
# hist = infy.history(period="1mo")

# print(hist)
# print(data["RELIANCE.NS"])
print(data)
df = pd.DataFrame(data)
df.to_csv("NBANK_yf.csv")


def get_data(codes, time_period="10y", interval="1mo"):

  data = yf.download(codes, period=time_period,
	interval=interval,
	group_by="ticker",
	auto_adjust=False)
  df = pd.DataFrame(data)
  return df
