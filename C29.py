List=[]

limit=100

for a in range(2,limit+1):
    for b in range(2,limit+1):
        n=a**b
        if not n in List:
            List+=[n]

print(len(List))
