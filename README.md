# Forecast-elicitation-Mechanism

Implement 4 papers:

- Water from Two Rocks: Maximizing the Mutual Information (MCG)
- Dominantly Truthful Multi-task Peer Prediction with a Constant Number of Tasks (DMI)
- A Bayesian truth serum for subjective data (BTS)
- Informed Truthfulness in Multi-Task Peer Prediction (CA)

# Usage

## To begin
You can install the package `femtools` using pip

	pip install femtools

To begin, import femtools

	import numpy as np
	import femtools as fem

## BTS
For Bayesian Truth Serum, we implemented the version with finite players. Call the function `BTS` with answers `x` and predicted frequencies `y`, score for every respondent is returned. `x` and `y` can be given in the `numpy.array` form or `list` form. If there are n respondents and m possible answers, `x` should be an n-dimensional vector and  each answer in `x` should be an integer in `[0, m)`. Similarly, `y` is a `n*m` matrix denoting the predicted frequencies. BTS score is composed of information-score and prediction score, thus optional parameter alpha controlling the weight given to the prediction score could be assigned between `(0,1]`. By default, `alpha` is `1`.

Here are examples

	>>> fem.BTS([3, 2, 1, 1, 0],
	... [[0.1, 0.1, 0.3, 0.5],
	... [0.1, 0.2, 0.5, 0.2],
	... [0.3, 0.4, 0.2, 0.1],
	... [0.3, 0.4, 0.1, 0.2],
	... [0.1, 0.3, 0.2, 0.4]])
	array([-3.28030172, -2.40787449, -0.29706308, -0.29706308, -1.074341  ])
	
	>>> fem.BTS([0, 0, 0],
	... [[0.5, 0.5],
	... [0.5, 0.5],
	... [0.5, 0.5]], alpha = 0.5)
	array([0.51873113, 0.51873113, 0.51873113])

## CA
For Correlated Agreement Mechanism, we implemented the detail-free version. CA Detail-Free is designed for multi-task problem with n agents and m tasks. Call the function `CA` with a `n*m` report matrix `reports`, score for every agent is returned. `reports` can be given in the `numpy.array` form or `list` form. For convenience, matrix `reports` can be given transposed with optional parameter `agent_first = False`. By default, `agent_first` is set to `True`. In addition, function `CA` does not expect that elements are integers.

Here is the example

	>>> fem.CA([['subway', 'subway', 'subway', 'burgerK', 'burgerK', 'burgerK'],
	... ['burgerK', 'McDonald', 'subway', 'McDonald', 'burgerK', 'burgerK'],
	... ['burgerK', 'McDonald', 'subway', 'McDonald', 'burgerK', 'burgerK'],
	... ['KFC', 'KFC', 'KFC', 'PizzaHot', 'McDonald', 'McDonald'],
	... ['PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'McDonald'],
	... ['PizzaHot', 'PizzaHot', 'PizzaHot', 'KFC', 'PizzaHot', 'subway'],
	... ['McDonald', 'McDonald', 'McDonald', 'McDonald', 'McDonald', 'McDonald'],
	... ['burgerK', 'burgerK', 'McDonald', 'burgerK', 'burgerK', 'burgerK'],
	... ['burgerK', 'subway', 'subway', 'PizzaHot', 'subway', 'subway'],
	... ['burgerK', 'burgerK', 'McDonald', 'burgerK', 'burgerK', 'burgerK'],
	... ['PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'PizzaHot', 'McDonald'],
	... ], agent_first = False)
	array([23, 20, 12, 23, 25, 25])

## DMI

Call the function `DMI` with answers `x` and the number of choices `C`. `x` should be given in the `numpy.array` form or `list` form. If there are n agents and m tasks,  `x` is a `n*m` matrix. Please make sure `m >= 2c` and each answer in `x` is an integer in `[0, c)`, otherwise the function will raise a `ValueError`.  DMI scores will return in `numpy.array` form.

Here is an example

```
>>> fem.DMI([[1, 1, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 0, 1]], 2)
array([1.5, 1.5])
```

## MCG

We implemented the multi-task common ground mechanism MCG(f) for Bernoulli distribution case. Call the function `MCG` with answers, function `f` and prior. The answers should be a `2*n` matrix in `numpy.array` form or `list` form for 2 agents' prediction and all the number in answers should in `[0, 1]`.  The prior is a number in `[0, 1]`, too. `f` should be in `["TVD", "KLD"]` for Total Variation Distance and KL divergence, respectively. By default, `f = "TVD"` . More functions will be supported in the future. The payments will return in `numpy.array` form.

Here is an example

```
>>> fem.DMI([[0.2, 0.3, 0.2], [0.3, 0.5, 0.3]], 'TVD', 0.3)
array([0.3333333333333333, 0.3333333333333333])
```

