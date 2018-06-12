#Challenge 4

def is_palindrome(n):
    s=list(str(n))
    if len(s)%2==0:
        length=len(s)/2;
    else:
        length=(len(s)+1)/2;
    for i in range(0,length):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

max_palin=0

for i in range(0,999):
    for j in range(0,999):
        product=i*j;
        if is_palindrome(product)==True and product>max_palin:
            max_palin=product;
print(max_palin);
