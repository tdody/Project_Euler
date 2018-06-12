# Challenge 13

with open ("C13.txt", "r") as myfile:
    data=myfile.read().replace('\n', ' ')
data_split=data.split();

sum_=0;
for i in range(0,len(data_split)):
    sum_=sum_+int(data_split[i]);
print(sum_)
