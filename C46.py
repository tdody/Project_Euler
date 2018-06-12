#Problem 46

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

n=27;
    
while True:
   if not is_prime(n):
       Test=0
       for k in primes_below(n):
           print(k)
           if (n-k)%2==0:
               print((n-k)%2)
               if int(((n-k)/2)**0.5)==((n-k)/2)**0.5:
                   print(int(((n-k)/2)**0.5))
                   print(((n-k)/2)**0.5)
                   Test=1
       if Test==0:
           print(n)
           break