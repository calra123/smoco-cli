
import pandas as pd
import numpy as np
from .stats import get_data
from texttable import Texttable

def winner_loser(dfperiodS, period):
    winners_a = []
    losers_a = []
    lenn = dfperiodS.shape[1] - 1
    for i in range(0,lenn):
        FH = dfperiodS.iloc[:,i:i+2]
        FH = FH.dropna().sort_values(by=FH.columns[0])

        winner = FH[FH.columns[1]].tail(5).mean()

        loser = FH[FH.columns[1]].head(5).mean()
        winners_a.append(winner)
        losers_a.append(loser)
    avg_winner = sum(winners_a)/len(winners_a)
    avg_loser = sum(losers_a)/len(losers_a)
    return [avg_winner, avg_loser, avg_winner - avg_loser]

def create_df(cleaned_df, period, names):
    dfperiodS = pd.DataFrame(index=cleaned_df.index[period-1::period], columns=names)
    dfperiodS.head()
    for name in names:
        dfperiodS[name] = cleaned_df[name, "Excess Returns"].rolling(period).sum()[period - 1::period]
    dfperiodS = dfperiodS.T
    return dfperiodS

def display_results(result):
    table = Texttable()
    table.header(['N X N', 'Winner', 'Loser', 'Winner - Loser'])
    for val in results:
        table.add_row([val+'X'+val, results[val]['winner'], results[val]['loser'], results[val]['w-l']])
    print(table.draw())



results = {}
time_intervals = ['3', '6', '12', '18', '24', '36']

def gen_analysis(data, nse_symbol):
    data.dropna(how='all', inplace=True)
    nifty = data
    nifty.drop(['Low', 'High', 'Adj Close', 'Volume'], level=1, axis=1, inplace=True)

    names = nifty.columns[::2].get_level_values(0)


    cleaned_df = nifty
    for name in names:
        cleaned_df[name, "Log C/O"] = np.log(cleaned_df[name, "Close"].astype(float)/cleaned_df[name, "Open"].astype(float))
    # names

    cleaned_df.sort_index(axis=1, inplace=True)

    # Matching Yahoo Finance symbol for index
    if nse_symbol[-3:] != ".NS":
        nse_symbol = "^"+nse_symbol
    niftyr = get_data(nse_symbol, symbol_only=True)


    niftyr["Log C/O"] = np.log(niftyr["Close"]/niftyr["Open"])

    niftyr.set_index(cleaned_df.index, inplace=True)

    #### Calculating Excess Returns ###

    for name in names:
        cleaned_df[name, "Excess Returns"] = cleaned_df[name, "Log C/O"].astype(float) - niftyr["Log C/O"].astype(float)

    cleaned_df.sort_index(axis=1, inplace=True)

    for val in time_intervals:
        n_df = create_df(cleaned_df, int(val), names)
        w, l, wl = winner_loser(n_df, int(val))
        results[val]= {'winner': float(f'{w:.4f}'), 'loser': float(f'{l:.4f}'), 'w-l': float(f'{wl:.4f}')}

    display_results(results)