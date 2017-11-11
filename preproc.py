
from collections import Counter
import numpy as np
import pandas as pd

def process_for_labels(ticker):
	hm_days = 7
	df = pd.read_csv('joined_closes.csv', index_col=0)
	tickers = df.columns.values.tolist()
	df.fillna(0, inplace=True)
	for i in range(1, hm_days+1):
		df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
	df.fillna(0, inplace=True)
	return tickers, df
	

def buy_sell_hold(*args):
	cols = [c for c in args]
	req = 0.02
	for col in cols:
		if col > req:
			return 1 # buy
		if col < -req:
			return -1 # sell
	return 0

def get_featuresets(ticker):
	hm_days = 7
	tickers, df = process_for_labels(ticker)
	df['{}_target'.format(ticker)] = list(map(buy_sell_hold, *[df['{}_{}d'.format(ticker, i)] for i in range(1, hm_days+1)]))

	vals = df['{}_target'.format(ticker)].values.tolist()
	str_vals = [str(i) for i in vals]
	print("Data spread for {}: ".format(ticker), Counter(str_vals))
	df.fillna(0, inplace=True)

	df = df.replace([np.inf, -np.inf], np.nan)
	df.dropna(inplace=True)
	df_vals = df[[ticker for ticker in tickers]].pct_change()
	df_vals = df_vals.replace([np.inf, -np.inf], 0)
	df_vals.fillna(0, inplace=True)

	X = df_vals.values
	y = df['{}_target'.format(ticker)].values

	return X, y, df

def all_featuresets(tickers):
	list = []
	for ticker in tickers:
		list.append(get_featuresets(ticker))
	return list

all_featuresets(process_for_labels('AAPL')[0])
