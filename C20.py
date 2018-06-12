# Challenge 20

n=1;
for i in range(1,101):
    n=n*i;
h=str(n);
sum_=0;
for k in range(0,len(h)):
    sum_=sum_+int(h[k]);
print(sum_)
