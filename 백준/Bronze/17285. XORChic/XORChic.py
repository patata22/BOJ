def findKey():
    temp=[]
    for x in chicken:
        temp.append(chr(ord(x)^key))

    if (''.join(temp))=="CHICKEN": return True
    return False
    

key=0
word=input()
chicken = word[0:7]
while True:
    if findKey():break
    key+=1
answer=[]
for x in word:
    answer.append(chr(ord(x)^key))
print(''.join(answer))
