dim=1001

resultat=1
n=1

for k in range (2,dim,2):
    for i in range(4):
        n+=k
        resultat+=n
print(resultat)
