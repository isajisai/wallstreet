import os
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style
from mpl_finance import candlestick_ohlc

print("Compiling stock data...")
directory = os.fsencode('stocks')

main_df = pd.DataFrame()
count = 0

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".csv"):
	    ticker = filename.replace('.csv', '')
	    df = pd.read_csv('stocks/' + filename)
	    df.set_index('Date', inplace=True)
	    df.rename(columns={'Adj Close' : ticker}, inplace=True)
	    df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)
	    main_df = main_df.join(df, how='outer')

	    count += 1
	    print("{}: Loaded {}".format(count, ticker))
	else:
	    continue

print(main_df.tail(16))
main_df.to_csv('joined_closes.csv')
