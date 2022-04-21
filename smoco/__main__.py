import sys
from .stats import get_data
from .cleaned_monthly import gen_analysis
import argparse

def main():
    print("SMOCO is a Stock Market Ananlysis Tool.\nCopyright "+u'\N{COPYRIGHT SIGN}'+" Himanshi Kalra")
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    choices = {}
    for arg in args:
        print('passed argument :: {}'.format(arg))
        if arg == "stats":
            print("Choose timeframe: \n")
            print("1. Last 10 years")
            print("2. Custom")

            i = input("Enter number: ")
            if 0 < int(i) <= 2:
                if i == "1":
                    choices['time_period'] = '10y'
                if i == "2":
                    print("Feature coming soon")
            else:
                print("Invalid input!")

        if arg == "index_symbol":
            print("Enter index symbol like NSEI(Nifty 50), NSEBANK(NIFTY BANK), CNXIT(NSE IT): ")
            choices['index_symbol'] = input("Enter symbol: ")

    data = get_data(choices['index_symbol'], time_period=choices['time_period'])

    gen_analysis(data, choices['index_symbol'])


if __name__ == '__main__':
    main()
