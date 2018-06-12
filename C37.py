#Problem 37

Counter=0
Sum=0
N=11

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

while Counter<11:
    if is_prime(N):
        Test=0
        for k in range(1,len(str(N))):
            if not is_prime(int(str(N)[:len(str(N))-k])):
                Test=1
            if not is_prime(int(str(N)[k:])):
                Test=1
        if Test==0:
            Counter+=1
            Sum+=N
            print(N)
    N+=2

print(Sum)

