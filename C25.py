# Challenge 25
fib_1=0;
fib_2=1;
sum_=0
total=0;
n=1;

while len(str(fib_2))<1000:
    sum_=fib_2+fib_1;
    if sum_%2==0:
        total=total+sum_;
    fib_1=fib_2;
    fib_2=sum_;
    n=n+1;
print(n)

