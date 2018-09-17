import os
import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd 
import pandas_datareader as web

import fix_yahoo_finance as yf
yf.pdr_override()

now = dt.datetime.now()
date = dt.datetime(now.year, now.month, now.day)
yesterday = dt.datetime(now.year, now.month, now.day-1)
directory = os.fsencode('stocks')
site = 'yahoo'

# FIXME: assumes Tesla will be in business in the future.
df = web.get_data_yahoo('TSLA')
print(df.head())

