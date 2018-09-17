import multiprocessing
import glob
import os
import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd 
import pandas_datareader.data as web

now = dt.datetime.now()
date = dt.datetime(now.year, now.month, now.day)
yesterday = dt.datetime(now.year, now.month, now.day-1)
directory = os.fsencode('stocks')
filenames = glob.glob("stocks/*.csv")

import fix_yahoo_finance as yf
yf.pdr_override()

def mp_worker(filename):
	ticker = filename.replace("stocks/", "").replace(".csv", "")
	df = web.get_data_yahoo(ticker, yesterday, date)
	if df is None:
		print('UNSUCCESSFUL UPDATE: {}'.format(ticker))
	df.to_csv('stocks/{}.csv'.format(ticker))
	print("SUCCESSFUL UPDATE: {}".format(ticker))

# def mp_handler():
# 	p = multiprocessing.Pool(100)
# 	p.map(mp_worker, filenames)

if __name__ == "__main__":
	for filename in filenames:
		mp_worker(filename)