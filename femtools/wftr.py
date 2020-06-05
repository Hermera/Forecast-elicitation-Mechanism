import numpy as np
import math

def comb(n, m):
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))

def dmi2(A1, B1, A2, B2, C):
    def check(x):
        return 0 <= x and x < C and type(x) == np.int64

    def GetM(A, B):
        assert(len(A) == len(B))
        M = np.zeros((C, C))
        for (x, y) in zip(A, B):
            if check(x) and check(y):
                M[x][y] += 1
            else:
                raise ValueError('The values of answers must be integers in [0, C)')
        return M

    M1 = GetM(A1, B1)
    M2 = GetM(A2, B2)

    return np.linalg.det(M1) * np.linalg.det(M2)

class functions:
    def __init__(self, a, b, c):
        self.f = a
        self.f_prime = b
        self.f_star = c
        
def TVD(t):
    return abs(t - 1)
def TVD_prime(x):
    x = math.log(x)
    if x > 0: return 1
    elif x == 0: return 0
    else: return -1
def TVD_star(x):
    return TVD_prime(x)
TVDs = functions(TVD, TVD_prime, TVD_star)

def KLD(t):
    return t * math.log(t)
def KLD_prime(t):
    return 1 + math.log(t)
def KLD_star(t):
    return t
KLDs = functions(KLD, KLD_prime, KLD_star)


def R(f, a, b, p):
    return f( a*b/p + (1-a)*(1-b)/(1-p) )

def MIG(answers, function, prior):
    if type(answers) == list:
        answers = np.array(answers)
        
    agent_n, task_n = answers.shape

    # N > 1;
    if agent_n != 2:
        raise ValueError('Invalid number of agents.')

    # f
    fs = TVDs
    if function == 'KLD':
        fs = KLDs

    # Calculate reward
    reward = 0
    penalty = 0
    for i in range(task_n):
        for j in range(task_n):
            if i == j:
                reward += R(fs.f_prime, answers[0][i], answers[1][i], prior)
            else:
                penalty += R(fs.f_star, answers[0][i], answers[1][j], prior)
    payment = reward / task_n - penalty / (task_n * (task_n - 1))

    return np.array([payment, payment])


if __name__ == '__main__':
    arr = np.array([[0.2, 0.3, 0.2], [0.3, 0.5, 0.3]])
    print(MIG(arr, 'TVD', 0.3))