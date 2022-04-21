
import pandas as pd
import numpy as np
from .stats import get_data

# data = get_data()
# nifty = pd.read_csv("monthly_cleaned.csv")
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


results = {}
time_intervals = ['3', '6', '12', '18', '24', '36']

def gen_analysis(data, nse_symbol):
    # data = data.dropna()
    nifty = data

    names = np.array(nifty.iloc[0,:].dropna().index)
    names = names[::6]

    index = pd.MultiIndex.from_product([names, ["Open", "Close"]], names=["Company name", "Information"])
    row_index = nifty.iloc[2:,0]
    row_index
    # #### Removing Row index and separting out data ####
    data_1 = nifty.iloc[:,1:]
    # Converted data into numpy array
    # data_1 = data_1[:].values
    data_1 = data_1.iloc[2:,::3].values
    cleaned_df = pd.DataFrame(data_1, index=row_index, columns=index)
    cleaned_df.index.name = "Year-Month"
    for name in names:
        cleaned_df[name, "Log C/O"] = np.log(cleaned_df[name, "Close"].astype(float)/cleaned_df[name, "Open"].astype(float))
    # names

    cleaned_df.sort_index(axis=1, inplace=True)

    ### Getting Index Data ###
    # niftyr = pd.read_csv("boss_N50.csv")
    niftyr = get_data(nse_symbol, symbol_only=true)

    niftyr["Log C/O"] = np.log(niftyr["Close"]/niftyr["Open"])

    niftyr.set_index(cleaned_df.index, inplace=True)

    # #### Calculating Excess Returns ###

    for name in names:
        cleaned_df[name, "Excess Returns"] = cleaned_df[name, "Log C/O"].astype(float) - niftyr["Log C/O"].astype(float)

    cleaned_df.sort_index(axis=1, inplace=True)


    # cleaned_df.to_csv("boss_excess_returnsN50.csv")

    # #### Strategy 3 X 3 ####

    # #### Creating dataframe for 3 X 3 strategy

    for val in time_intervals:
        n_df = create_df(cleaned_df, int(val), names)
        results[val]['winner'], results[val]['loser'], results[val]['w-l'] = winner_loser(n_df, int(val))

    for val in time_intervals:
        print(results[val])

    # threeS = pd.DataFrame(index=cleaned_df.index[2::3], columns=names)
    # threeS.head()

    # # ### Taking cumulative sum for every 3 months
    # # #### 3 Months - Formation, 3 Months - Holding

    # for name in names:
    #     threeS[name] = cleaned_df[name, "Excess Returns"].rolling(3).sum()[2::3]


    # threeS.iloc[:2,].sum()

    # # threeSshort = pd.DataFrame(index=names, columns = threeS.index)

    # # #### Taking Transpose for better visualization

    # dfT = threeS.T

    # dfT.head()

    # # dfT.rolling(2).sum()
    #  [markdown]
    # # ### Sorting values to classify Winner and Loser Stocks

    # winners_a = []
    # losers_a = []
    # for i in range(0,39):
    #     FH31 = dfT.iloc[:,i:i+2]
    # #     print(i)
    # # FH31.dropna()
    #     FH31 = FH31.dropna().sort_values(by=FH31.columns[0])
    #     winner = FH31[FH31.columns[1]].tail().mean()
    #     loser = FH31[FH31.columns[1]].head().mean()
    #     winners_a.append(winner)
    #     losers_a.append(loser)
    # #     print(winners_a)
    # avg_winner = sum(winners_a)/len(winners_a)
    # avg_loser = sum(losers_a)/len(losers_a)
    # # FH31.head()
    # #Loser Stocks

    # avg_loser

    # avg_winner

    # avg_winner - avg_loser

    # # FH31["9/1/2012"].tail()
    # # Winner Stocks
    # # FH31.head()


    #  [markdown]
    # # 6 X 6 Strategy

    # sixS = pd.DataFrame(index=cleaned_df.index[5::6], columns=names)
    # sixS.head()
    # for name in names:
    #     sixS[name] = cleaned_df[name, "Excess Returns"].rolling(6).sum()[5::6]
    # sixST = sixS.T
    # sixST.shape[1]
    # sixST.head()

    # winners_a = []
    # losers_a = []
    # lenn = sixST.shape[1] - 1
    # for i in range(0,lenn):
    #     FH61 = sixST.iloc[:,i:i+2]
    # #     print(i)
    # # FH31.dropna()
    #     FH61 = FH61.dropna().sort_values(by=FH61.columns[0])
    #     winner = FH61[FH61.columns[1]].tail(5).mean()
    # #     print(winner)
    #     loser = FH61[FH61.columns[1]].head(5).mean()
    #     winners_a.append(winner)
    #     losers_a.append(loser)
    # avg_winner = sum(winners_a)/len(winners_a)
    # avg_loser = sum(losers_a)/len(losers_a)

    # avg_winner

    # avg_loser

    # avg_winner - avg_loser
    #  [markdown]
    # # #### 12 X 12 Strategy

    # twelveS = pd.DataFrame(index=cleaned_df.index[11::12], columns=names)
    # twelveS.head()
    # for name in names:
    #     twelveS[name] = cleaned_df[name, "Excess Returns"].rolling(12).sum()[11::12]
    # twelveST = twelveS.T
    # twelveST.shape[1]
    # twelveST.head()

    # winners_a = []
    # losers_a = []
    # lenn = twelveST.shape[1] - 1
    # for i in range(0,lenn):
    #     FH12 = twelveST.iloc[:,i:i+2]
    #     FH12 = FH12.dropna().sort_values(by=FH12.columns[0])
    #     winner = FH12[FH12.columns[1]].tail().mean()
    # #     print(winner)
    #     loser = FH12[FH12.columns[1]].head().mean()
    #     winners_a.append(winner)
    #     losers_a.append(loser)
    # avg_winner = sum(winners_a)/len(winners_a)
    # avg_loser = sum(losers_a)/len(losers_a)

    # avg_winner - avg_loser

    # avg_winner

    # avg_loser
    # # #### 24 X 24 Strategy

    # S24 = create_df(cleaned_df, 24)

    # cleaned_df["ADANIPORTS.NS", "Log C/O"].sum()

    # # cleaned_df["ADANIPORTS.NS"].tail()
    # np.log(2522/2409)

    # cleaned_df["ADANIPORTS.NS"].tail()

    # cleaned_df.head()

    # S24.head()



    # W24, L24, WL24 = winner_loser(S24, 24)

    # WL24

    # W24

    # L24
    #  [markdown]
    # # #### 36 X 36 Strategy

    # S36 = create_df(cleaned_df, 36)
    # W36, L36, WL36 = winner_loser(S36, 36)

    # WL36

    # W36

    # L36

    # S9 = create_df(cleaned_df, 9)
    # W9, L9, WL9 = winner_loser(S9, 9)

    # WL9

    # W9

    # L9

    # S18 = create_df(cleaned_df, 18)
    # W18, L18, WL18 = winner_loser(S18, 18)

    # W18

    # WL18

    # L18

