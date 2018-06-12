#Problem 35

circular=set()
import itertools
import math

def primes_below(end):
    if end < 2:
        return []

    lng = (end//2) - 1
    primes = [True]*lng  

    for i in range(int(lng**0.5)):  
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False  

    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


List=primes_below(1000000)

for k in List:
    if k<10:
        circular.add(k)
    else:
        sub_list=[int(i) for i in str(k)]
        Test=0
        if 2 in sub_list or 5 in sub_list or 0 in sub_list or 4 in sub_list or 6 in sub_list or 8 in sub_list:
            Test=1
        if Test==0:
            N=''.join(str(elem) for elem in sub_list)
            for k in range(1,len(N)+1):
                if Test==0 and is_prime(N):
                    N=int(str(N)[1:]+str(N)[0])
                else:
                    Test=1
            if Test==0:
                circular.add(int(N));
print(len(circular));
