# Challenge 23
def divisor(n):
    divisor_sum=0;
    for k in range(1,n):
        if (n%k)==0:
            divisor_sum=divisor_sum+k;
    return divisor_sum;

def is_abundant(n):
    if n>divisor(n):
        return False
    else:
        return True

list_=[];

for i in range(0,28124):
    if is_abundant(i)==False:
        list_.append(i);
print(list_);


##sum_=0;
##
##for i in range(1,28123+1):
##    for j in range(1,28123-i):
##        if is_abundant(i)==True and is_abundant(j)==True:
##            continue
##        else:
##            sum_=sum_+i+j;
##print(sum_);
