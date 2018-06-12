#Problem 41
#We shall say that an n-digit number is pandigital if it makes use of all the
#digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
#also prime.
#What is the largest n-digit pandigital prime that exists?


def is_pandigital(n):
    n=str(n);
    s=len(n);
    Int=''
    for x in range(0,s):
        Int+=str(x+1)
    for k in Int:
        if not k in n:
            return False
    return True
    
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

end=10**8

List=primes_below(end)

for k in range(len(List)-1,0,-1):
    if is_pandigital(List[k]):
        print(List[k])
        break