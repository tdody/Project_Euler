# Challenge 2
fib_1=0;
fib_2=1;
sum_=0
total=0;

while fib_2<4000000:
    sum_=fib_2+fib_1;
    if sum_%2==0:
        total=total+sum_;
    fib_1=fib_2;
    fib_2=sum_;
print(total)

