# Challenge 21

def divisor(n):
    divisor_sum=0;
    for k in range(1,n):
        if (n%k)==0:
            divisor_sum=divisor_sum+k;
    return divisor_sum;

global_sum=0;
for k in range(1,10001):
    if k==divisor(divisor(k)) and not(k==divisor(k)):
        print(k)
        global_sum=global_sum+k;
print(global_sum);
