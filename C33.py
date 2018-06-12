#Problem 33
from __future__ import division

def is_simple(a,b):
    a1=int(str(a)[0]);
    a2=int(str(a)[1]);
    b1=int(str(b)[0]);
    b2=int(str(b)[1]);
    if b<a:
        return False
    else:
        if a1==b1 and not a2==0 and not a1==0 and not b2==0:
            if float(a/b)==float(a2/b2):
                return True
        if a1==b2 and not a2==0 and not a1==0 and not b1==0:
            if float(a/b)==float(a2/b1):
                return True
        if a2==b1 and not a2==0 and not a1==0 and not b2==0:
            if float(a/b)==float(a1/b2):
                return True
        if a2==b2 and not a2==0 and not a1==0 and not b1==0:
            if float(a/b)==float(a1/b1):
                return True
        else:
            return False
        
for b in range(11,100):
    if not b//10==0:
        for a in range(11,b):
            if is_simple(a,b):
                print(a,b)
