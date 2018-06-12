#Problem 42

def word_to_number(string):
    word= string.lower()
    total=0
    for k in list(word):
        total+=(ord(k)-96);
    return(total)

f=open('word.txt','r')
listWord=(f.read())
listWord=listWord.split(',')

listNumber=[]
for h in range(0,len(listWord)):
    listNumber.append(word_to_number(listWord[h]))

def is_triangle(K):
    for n in range(1,int((2*K)**0.5)+1):
        if 0.5*n*(n+1)==K:
            return True
    return False

total=0

for n in range(0,len(listWord)):
    if is_triangle((word_to_number(listWord[n]))):
        total+=1
print(total)