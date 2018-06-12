# Challenge 18
with open ("C18.txt", "r") as myfile:
    data=myfile.read()
data_split=data.split('\n');

for i in range(0,len(data_split)):
    data_split[i]=data_split[i].split(' ');

for i in range(0,len(data_split)):
    for j in range(0,len(data_split[i])):
        data_split[i][j]=int(data_split[i][j]);

for k in range(len(data_split)-1,-1,-1):
    clone=[];
    for h in range(0,len(data_split[k])-1):
            clone.append(max(data_split[k][h],data_split[k][h+1]));
    if not(k==0):
        for j in range(0,len(data_split[k-1])):
            data_split[k-1][j]=data_split[k-1][j]+clone[j];
print(data_split[0][0]);
