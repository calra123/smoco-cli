import json
import yfinance as yf
import pandas as pd

def get_symbol_codes(nse_symbol):

    f = open('index_symbols.json')
    fdata = json.load(f)
    symbol_list = fdata[nse_symbol]

    string_codes_list = " ".join(symbol_list)
    return string_codes_list


def get_data(nse_symbol, time_period="10y", interval="1mo", symbol_only=False):

    if symbol_only:
        codes = nse_symbol
    else:
        codes = get_symbol_codes(nse_symbol)
    data = yf.download(codes, period=time_period,
        interval=interval,
        group_by="ticker",
        auto_adjust=False)
        df = pd.DataFrame(data)
    return df