#Problem 36

def is_palindrome(N):
    N=str(N)
    for k in range(0,len(N)):
        if not N[k]==N[len(N)-k-1]:
            return False
    return True

Sum=0
for x in range (1000000,0,-1):
    if is_palindrome(int(bin(x)[2:])) and is_palindrome(x):
        print x
        Sum+=x
print(Sum)
