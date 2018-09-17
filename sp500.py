
import shutil
import os
import pandas as pd
import pandas_datareader.data as web
import datetime as dt

if os.path.exists('stocks/'):
		shutil.rmtree('stocks/')
os.mkdir('stocks/')
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
df.columns = df.ix[0] 
df.drop(df.index[0], inplace=True)
now = dt.datetime.now()

src = 'yahoo'
start = dt.datetime(2000, 1, 1)
end = dt.datetime(now.year, now.month, now.day)

import fix_yahoo_finance as yf
yf.pdr_override()

def retrieve_dframe(ticker, start, end, tries_left):
	if tries_left == 0:
		return None
	try: 
		return web.get_data_yahoo(ticker, start, end)
	except:
		return retrieve_dframe(ticker, start, end, tries_left-1)

def make_csv(ticker, src, start, end):
	ticker = ticker.replace('.', '-')
	ds = retrieve_dframe(ticker, start, end, 10)
	if ds is None:
		print('UNSUCCESSFUL LOAD: ' + ticker)
		return
	else:
		if not os.path.exists('stocks/{}.csv'.format(ticker)): 
			ds.to_csv('stocks/{}.csv'.format(ticker))
			print('Successfully loaded: ' + ticker)
		else:
			print('Already loaded: ' + ticker)
		return

for value in df.values:
	ticker = value[0]
	make_csv(ticker, src, start, end)

