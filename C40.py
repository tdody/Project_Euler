#Problem 40

STR=''

for i in range(1,1000000):
    STR+=str(i)
product=int(STR[0])*int(STR[9])*int(STR[99])*int(STR[999])*int(STR[9999])*int(STR[99999])*int(STR[999999])
print(product)
