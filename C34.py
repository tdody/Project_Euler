#Problem 34

import math

Total=0

for a in range(3,2540160):
    list=[]
    list=[int(i) for i in str(a)]
    sum=0
    for b in list:
        sum+=math.factorial(b)
    if sum==a:
        Total+=a
print(Total)
