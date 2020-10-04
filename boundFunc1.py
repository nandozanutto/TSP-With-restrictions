def boundAux(A, x, W):
    min = float("inf")
    for y in W:
        if ((x!=y) and (A[x][y]) <= min):
            min = A[x][y]
    return min


def bound1(A, X, n):
    l = len(X)
    if(l<1): return -1
    if(l==n): return cost(A, X)
    total = 0

    y = [i for i in range(n) if i not in X]

    for i in range(l-1):
        total += A[X[i]][X[i+1]]

    total += boundAux(A, X[-1], y)

    y_aux = y + [0]
    for i in y:
        total += boundAux(A, i, y_aux)

    return total


def wrongOrder(X, destiny, order):
    for i in order:
        if (destiny == i[1]) and (i[0] not in X):
            return True
    return False


def callingBound2(A, choices, n, X, order):
    for choice in choices:
        X_aux = X + [choice[0]]
        choice[1] = bound2(A, X_aux, n, order)

def bound2(A, X, n, order):
    l = len(X)
    if (l < 1): return -1
    if (l == n): return cost(A, X)
    total = 0

    y = [i for i in range(n) if i not in X]
    column1 = [i[0] for i in order]
    column2 = [i[1] for i in order]

    for i in range(l - 1):
        total += A[X[i]][X[i + 1]]


    y_aux = y[:]
    for element in order:
        if element[0] not in X and element[1] in y_aux:
            y_aux.remove(element[1])


    total += boundAux(A, X[-1], y_aux)


    for i in y:
        if i in column1:
            y_aux = y[:]
        else:
            y_aux = y + [0]

        if i in column2:
            try:
                y_aux.remove(column1[column2.index(i)])
            except ValueError:
                pass

        total += boundAux(A, i, y_aux)

    return total

def cost(A, X):
    sum = 0
    for i in range(0, len(X) - 1):
        sum += A[X[i]][X[i + 1]]
    return sum + A[X[-1]][X[0]]


