#Problem 43

def is_pandigital(n):
    s=len(n);
    Int=''
    for x in range(0,s):
        Int+=str(x+1)
    for k in Int:
        if not k in n:
            return False
    return True
    
d5d6d7d8d9d10=['952867','357289']
candidate=['4310','6410']

Total=0

def permutations(word):
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(str(perm[:i] + char + perm[i:]))
    return result
    
    
def check(n):
    if int(n[1:4])%2==0 and int(n[2:5])%3==0:
        return True
    return False
    
    
for N in range(0,2):
    for per in permutations(candidate[N]):
        for k in range(0,2):
            final=per+d5d6d7d8d9d10[k]
            if is_pandigital(final) and check(final):
                Total+=int(final)
print(Total)