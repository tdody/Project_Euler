# Challenge 3

prime_list=[2];

def is_prime(n):
    for number in range(2,n):
        if (n%number)==0:
            return False
    return True

i=2;
Goal=600851475143;
sum_prime=0;

while i<=Goal:
    if Goal%i==0:
        if is_prime(i)==True:
            Goal=Goal/i
    i=i+1;
print(i-1)
