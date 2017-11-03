
import os
import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd 
import pandas_datareader as web

now = dt.datetime.now()
date = dt.datetime(now.year, now.month, now.day)
yesterday = dt.datetime(now.year, now.month, now.day-1)
directory = os.fsencode('stocks')
site = 'yahoo'

df = web.get_data_yahoo('TSLA')
print(df.head())
