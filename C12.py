# Challenge 11
import math

def numb_divisor(n):
    divisor=0;
    i=1;
    sqrt=int(math.sqrt(n));
    while i<=sqrt:
        if (n%i)==0:
            divisor=divisor+2
        i=i+1;
    if sqrt*sqrt==n:
        divisor=divisor-1;
    return divisor;




i=0;
n=0;
while True:
    n=n+1;
    i=i+n;
    if numb_divisor(i)>500:
        break
print(i);
    
