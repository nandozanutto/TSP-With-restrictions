import numpy as np
import random

def createA(n):
    A = np.random.randint(1, high=100, size=(n, n))
    for i in range(n):
        A[i][i] = 0
    return A

def createOrder(n):
    num = random.randint(1, n)
    order = []
    for i in range(2):
        res = random.sample(range(1, n), 2)
        order.append(res)

    return order

