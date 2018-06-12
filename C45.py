#Problem 45

def is_pentagonal(K):
    X=int((0.5+(0.25+6*K)**0.5)/3)
    if X*(3*X-1)/2==K:
        return True
    return False
    
def is_triangle(K):
    X=int((-0.5+(0.25+2*K)**0.5))
    if X*(X+1)/2==K:
        return True
    return False
    
def is_hexagonal(K):
    X=int((1+(1+8*K)**0.5)/4)
    if X*(2*X-1)==K:
        return True
    return False    

n=144;
    
while True:
    n+=1
    k=n*(2*n-1)
    if is_pentagonal(k):
        if is_triangle(k):
            print(k)
            break