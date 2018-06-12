#Challenge 10

def is_prime(n,List):
    for number in List:
        if (n%number)==0:
            return False
    return True

i=3;
target=2000000;
sum_prime=2;
List_prime=[2];

while i<target:
    if is_prime(i,List_prime)==True:
        List_prime.append(i);
        sum_prime=sum_prime+i;
    i=i+2;
print(sum_prime);
        
