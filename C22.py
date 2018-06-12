# Challenge 22

with open ("Names.txt", "r") as myfile:
    data=myfile.read()
data_split=data.split(',');

data_split.sort()

sum_global=0;

for i in range(0,len(data_split)):
    sum_=0;
    for k in data_split[i]:
        sum_=sum_+ord(k.lower())-96;
    sum_global=sum_global+sum_*(i+1);
