#Problem 32

def is_pandigital(n,s):
    n=str(n);
    if len(n)==s:
        for k in '123456789':
            if not k in n:
                return False
    return True
 
p=set();
 
for i in range(2,100):
    start=1234 if i<10 else 123
    for j in range(start,10000//i):
        if is_pandigital(str(i)+str(j)+str(i*j),9):
            p.add(i*j)
            print(p)
print(sum(p))
