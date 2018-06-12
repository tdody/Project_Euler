#Challenge 9

for c in range(0,1000):
    for b in range(0,1000-c):
        a=1000-c-b;
        if a>=0:
            if (a*a+b*b)==c*c:
                print(a*b*c);
                break;
                
