import boundFunc1 as b1
from timeit import default_timer as time


OptC = float("inf")
OptX = []
nodes = 0

def resetGlobal():
    global OptC, OptX, nodes
    OptC = float("inf")
    OptX = []
    nodes = 0

def callingTSP2(A, n, order, second):
    resetGlobal()
    X = []
    C = []
    start_time = time()
    TSP2(A, 0, X, C, n, order, second)
    end_time = time()
    final_time = end_time - start_time
    final_time = final_time * 1000
    return (OptC, OptX, final_time, nodes)

def TSP2(A, l, X, C, n, order, second):
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

    choices = []
    for i in C[l]:
        X_aux = X + [i]
        aux = [i, b1.bound1(A, X_aux, n)]
        choices.append(aux)

    choices.sort(key=lambda choice: choice[1])
    if(second):
        b1.callingBound2(A, choices, n, X, order)


    for i in choices:
        if b1.wrongOrder(X, i[0], order):
            continue
        if(i[1] >= OptC):
            continue#need to change
        newX = X + [i[0]]
        TSP2(A, l+1, newX, C, n, order, second)