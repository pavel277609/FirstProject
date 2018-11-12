import copy
import random
import sys

l=[2, 3, [4, 5]]
l2=l.copy()
l2[0]=88
l2[2][1]=30
print(l)
print(l2)

x = [1, 3 , [6,7]]
y = []

y = copy.deepcopy(x)

y.append(6)
y[2].append(8)
print(x)
print(y)

print(id(x))
print(id(y))

print(random.random())

print(sys.version)
print(sys.platform)



