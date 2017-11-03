

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
site = 'yahoo'

print("Updating...")
def retrieve_dframe(ticker, src, start, end, tries_left):
	if tries_left == 0:
		return None
	try:
		print("Trying...")
		return web.DataReader(ticker, src, start, end)
	except:
		print("Nope.")
		return retrieve_dframe(ticker, src, start, end, tries_left-1)

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".csv"):
	    ticker = filename.replace('.csv', '')
	    print('{}'.format(ticker))
	    df = retrieve_dframe(ticker, site, yesterday, date, 10)
	    if df is None:
	    	print('UNSUCCESSFUL UPDATE: {}', ticker)
	    	continue
	    else:
	    	print(df.head())
	    	# print('Successful update: {}', ticker)