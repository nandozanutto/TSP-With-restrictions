#!/usr/bin/python2
import TSP2 as t2
import inputs as inp
import sys
import readData as read
import OrderAux as Ord


# creating random inputs
# n = 10
# A = inp.createA(n)
# order = inp.createOrder(n)

A, n, m, order = read.get()

# using checkOrder optimization
# if(Ord.checkOrder(order)):
#     print("inf")
#     sys.stderr.write("{} nodes\n{} ms\n".format(0, 0))
#     sys.exit()


if (len(sys.argv) > 1 and sys.argv[1] == '-a'):
    OptC, OptX, final_time, nodes = t2.callingTSP2(A, n, order, False)
else:
    OptC, OptX, final_time, nodes = t2.callingTSP2(A, n, order, True)

print(OptC)
for i in range(1, len(OptX)):
    print(OptX[i])


sys.stderr.write("{} nodes\n{} ms\n".format(nodes, final_time))
