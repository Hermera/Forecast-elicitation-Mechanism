import numpy as np

def BTS(x, y, alpha = 1.0):
	x, y = np.array(x), np.array(y)
	n, m = y.shape

	_xbar = np.zeros([m], dtype = float)
	_ybar = np.zeros([m], dtype = float)
	for opinion in x:
		_xbar[opinion] += 1.0
	for player in y:
		_ybar += np.log(player)
	def xbar(k, r, s):
		#return _xbar[k] / n
		return (_xbar[k] + 1 - float(x[r] == k) - float(x[s] == k)) / (n + m - 2)
	def ybar(k, r, s):
		#return _ybar[k] / n
		return (_ybar[k] - np.log(y[r][k]) - np.log(y[s][k])) / (n - 2)

	score = np.zeros([n], dtype = float)
	for r in range(n):
		info, pred = 0.0, 0.0
		for s in range(n):
			if r == s: continue
			info += np.log(xbar(x[r], r, s)) - ybar(x[r], r, s)
			for k in range(m):
				pred += xbar(k, r, s) * np.log(y[r][k] / xbar(k, r, s))
		score[r] = info + pred * alpha
	return score


if __name__ == '__main__':
	score = BTS([0 for i in range(100 - 1)] + [1], [[0.99, 0.01] for i in range(100)])
	print(score.sum())

	score = BTS([3, 2, 1, 1, 0],
	[[0.1, 0.1, 0.3, 0.5],
	[0.1, 0.2, 0.5, 0.2],
	[0.3, 0.4, 0.2, 0.1],
	[0.3, 0.4, 0.1, 0.2],
	[0.1, 0.3, 0.2, 0.4]])
	print(score, score.sum())

	score = BTS([0, 0, 0],
	[[0.5, 0.5],
	[0.5, 0.5],
	[0.5, 0.5]])
	print(score, score.sum())