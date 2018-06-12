def primes_below(end):
    if end < 2:
        return []

    lng = (end//2) - 1
    primes = [True]*lng  

    print(int(lng**0.5));
    for i in range(int(lng**0.5)):
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False  

    #return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]
#primes_below(10)
lng = (10//2) - 1
i=0
print(2*i*(i+3)+3);
print(lng);
print(2*i+3)
for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
    print(j); 
