def sum_digits_fifth_powers(nb):
    sum = 0
    for i in str(nb):
        sum += int(i)**5
    return sum

resultat = 0

for i in range(2, 354295):
    if i == sum_digits_fifth_powers(i):
        resultat += i

print(resultat)
