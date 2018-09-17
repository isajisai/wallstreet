def amean(lst):
	summ = 0
	for item in lst:
		summ += item
	return summ / len(lst)

def gmean(lst):
	product = 1
	for item in lst:
		product *= item
	return product ** (1 / len(lst))

def stddev(lst):
	mean = amean(lst)
	summ = 0
	for item in list:
		summ += (item - mean) ** 2
	return (summ * (1 / len(lst))) ** 0.5

def cron_alpha(lst):
	std = stddev(lst)
	summ = 0
	k = len(lst)
	for item in lst:
		summ += item
	return (k / (k - 1)) * (1 - (summ / std))

