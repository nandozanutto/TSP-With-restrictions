import boundFunc1 as b1
import time

OptC = float("inf")
OptX = []
nodes = 0

def callingTSP1(A, n, order):
    X = []
    C = []
    start_time = time.time()
    TSP1(A, 0, X, C, n, order)
    end_time = time.time()
    return (OptC, OptX, end_time - start_time, nodes)

def TSP1(A, l, X, C, n, order):
    global OptC
    global OptX
    global nodes
    nodes += 1
    if(l==n):
        c = b1.cost(A, X)
        if(c < OptC):
            OptC = c
            OptX = X[:]
        return

    if(l==0):
        try:
            C[l] = [0]
        except IndexError:
            C.append([0])

    else:
        if(l==1):
            try:
                C[l] = range(1, n)
            except IndexError:
                C.append(range(1, n))
        else:
            aux = C[l-1][:]
            aux.remove(X[l - 1])
            try:
                C[l] = aux[:]
            except IndexError:
                C.append(aux[:])

    B = b1.bound1(A, X, n)
    for i in C[l]:
        if b1.wrongOrder(X, i, order):
            continue
        if B >= OptC:
            return
        newX = X[:]
        newX.append(i)
        TSP1(A, l+1, newX, C, n, order)

