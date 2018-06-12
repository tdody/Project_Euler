#Challenge 7

def is_prime(n):
    for number in range(2,n):
        if (n%number)==0:
            return False
    return True

i=1;
target=2000000
sum_prime=0;

for i in range(1,target)
    if is_prime(i)==True:
        sum_prime=sum_prime+i;
print(sum_prime);
        
