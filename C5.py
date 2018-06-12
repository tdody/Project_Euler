#Challenge 5

List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
i=1;
tracker=1;

while True:
    for j in List:
        if tracker==1:
            if i%j!=0 or i/j<1:
                tracker=0;
    if tracker==1:
        break
    else:
        i=i+1
        tracker=1;

            
