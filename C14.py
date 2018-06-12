# Challenge 14

def is_odd(n):
    if (n%2)==0:
        return False
    else:
        return True

def chain(n):
    if is_odd(n)==True:
        n=3*n+1;
    else:
        n=n/2;
    return n


max_chain=0;
max_N=0
for i in range(2,1000001):
    N=i
    chain_length=1;
    while not(i==1):
        i=chain(i);
        chain_length=chain_length+1;
    if chain_length>max_chain:
        max_chain=chain_length;
        max_N=N;
print(max_chain);
print(max_N);
