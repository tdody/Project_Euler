with open ("C11.txt", "r") as myfile:
    data=myfile.read().replace('\n', ' ')
data_split=data.split();

for i in range(0,len(data_split)):
    data_split[i]=int(data_split[i]);

# Lines
# 20 caracters per lines
max_lines=0;
lines_product=1;
for i in range(0,20):
    for j in range(0,17):
        for k in range(0,4):
            lines_product=lines_product*data_split[i*20+j+k];
        if lines_product>max_lines:
            max_lines=lines_product;
        lines_product=1;
print(max_lines);
        

# Columns
# 20 caracters per columns
max_columns=0;
columns_product=1;
for i in range(0,17): #column
    for j in range(0,20): #lines
        for k in range(0,4): #lines
            columns_product=columns_product*data_split[i*20+j+k*20];
        if columns_product>max_columns:
            max_columns=columns_product;
        columns_product=1;
print(max_columns);


# Diagonals/
max_diag=0;
diag_product=1;
for i in range(3,21): #column
    for j in range(0,17): #line
        for k in range(0,4):
            diag_product=diag_product*data_split[(i-k)+(j+k-1)*20];
        if diag_product>max_diag:
            max_diag=diag_product;
        diag_product=1;
print(max_diag);
# Diagonals/
