import sys
import numpy as np


def get():
    data = sys.stdin.read()  # reading from stdin
    inputs = map(int, data.split())
    n = inputs[0] + 1
    m = inputs[1]
    aux = n * n + 2
    A = np.array(inputs[2:aux]).reshape(n, n)
    order = []
    del inputs[0:aux]
    while (len(inputs) > 0):
        order.append(inputs[0:2])
        del inputs[0:2]
    return A, n, m, order
