import sys
from .stats import get_data
# from .classmodule import MyClass
# from .funcmodule import my_function

def main():
    print("Hello wow")
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
            choices['symbol_name']

    data = get_data(choices['index_symbol'], time_period=choices['time_period'])

    analysis = gen_analysis(data, nse_symbol)




    # my_function('hello world')

    # my_object = MyClass('Thomas')
    # my_object.say_name()

if __name__ == '__main__':
    main()
