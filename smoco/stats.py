import json
import yfinance as yf
import pandas as pd

# fpath = "smoco/index_symbols.json"
# f = open(fpath, 'r')
# fdata = json.load(f)

def get_symbol_codes(nse_symbol):
    fpath = "smoco/index_symbols.json"
    f = open(fpath, 'r')
    fdata = json.load(f)

    symbol_list = fdata[nse_symbol]
    list_codes_string = " ".join(symbol_list)
    f.close()
    return list_codes_string


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