import numpy as np

def CA(reports, agent_first = True):
	reports = np.array(reports)
	if agent_first:
		reports = reports.transpose()
	m, n = reports.shape # m agents n tasks
	options = np.unique(reports)
	option_index = {}
	for key, item in enumerate(options):
		option_index[item] = key

	#separate tasks
	groupA = np.random.choice(m, m // 2, replace = False)
	groupB = np.setdiff1d(np.arange(0, m), groupA)
	def learning(reports):
		k = options.shape[0]
		joint = np.zeros([k, k], dtype = float)
		alpha = 1.0 / reports.shape[0]
		for task in reports:
			sample = np.random.choice(task, 2, replace = False)
			i = option_index[sample[0]]
			j = option_index[sample[1]]
			joint[i][j] += alpha
		marginal = joint.sum(axis = 1)
		return joint - np.matmul(marginal.reshape(k, 1), marginal.reshape(1, k))

	DeltaA = learning(reports[groupA, :]) > 0
	DeltaB = learning(reports[groupB, :]) > 0

	score = np.zeros([n], dtype = int)
	def scorer(reports, scoreMatrix):
		for task in reports:
			for agent1 in range(n):
				for agent2 in range(agent1):
					report1 = option_index[task[agent1]]
					report2 = option_index[task[agent2]]
					if scoreMatrix[report1][report2]:
						score[agent1] += 1
						score[agent2] += 1
		return 

	scorer(reports[groupA, :], DeltaB)
	scorer(reports[groupB, :], DeltaA)
	return score

if __name__ == '__main__':
	reports = np.array([np.random.choice(
		['subway', 'burgerK', 'McDonald', 'KFC', 'PizzaHot'], 100, p=[0.1, 0.2, 0.2, 0, 0.5]) for x in range(8)])
	CA(reports)

	CA([['subway', 'subway', 'subway', 'burgerK', 'burgerK', 'burgerK'],
		['burgerK', 'McDonald', 'subway', 'McDonald', 'burgerK', 'burgerK'],
		['burgerK', 'McDonald', 'subway', 'McDonald', 'burgerK', 'burgerK'],
		['KFC', 'KFC', 'KFC', 'PizzaHot', 'McDonald', 'McDonald'],
		['PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'McDonald'],
		['PizzaHot', 'PizzaHot', 'PizzaHot', 'KFC', 'PizzaHot', 'subway'],
		['McDonald', 'McDonald', 'McDonald', 'McDonald', 'McDonald', 'McDonald'],
		['burgerK', 'burgerK', 'McDonald', 'burgerK', 'burgerK', 'burgerK'],
		['burgerK', 'subway', 'subway', 'PizzaHot', 'subway', 'subway'],
		['burgerK', 'burgerK', 'McDonald', 'burgerK', 'burgerK', 'burgerK'],
		['PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'McDonald'],
		], agent_first = False)

