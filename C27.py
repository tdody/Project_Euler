def primes_below(end):
    if end<2:
        return []
    # For all numbers <end, only end//2 prime number can exist (All odd numbers)
    # 2 is removed from the list

    # Max number of primes
    lng=(end//2)-1

    # Create a list of True/False lond of lng
    primes=[True]*lng

    # Since we are removing from the list using a A*B criteria,
    # only half of the list is tested since A*B=B*A
    for i in range(int(lng**0.5)):
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False  

    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

def is_prime(nb):
    if nb <= 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

primes=primes_below(1000)
longest=0

for b in primes:
    for a in range(-999,999,2):
        image=b
        n=0
        while is_prime(image):
            n+=1
            image=n**2+a*n+b
        if n>longest:
            longest=n
            resultat=a*b
print(resultat)
    
