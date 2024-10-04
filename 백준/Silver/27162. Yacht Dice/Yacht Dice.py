def calc():
    result=0
    for i in range(1,7):
        if cmd[i-1]:
            result=max(result,i*count[i])
    if cmd[6]:
        result=max(result,fkCalc())
    if cmd[7]:
        result=max(result,fhCalc())
    if cmd[8]:
        result=max(result,lsCalc())
    if cmd[9]:
        result=max(result,bsCalc())
    if cmd[10]:
        result=max(result,yacht())
    if cmd[11]:
        result=max(result,sum(number))
    return result

def fkCalc():
    for i in range(1,7):
        if count[i]==4:return 4*i
    return 0

def fhCalc():
    for i in range(1,7):
        for j in range(1,7):
            if count[i]==3 and count[j]==2:
                return 3*i+2*j
    return 0

def lsCalc():
    for i in range(1,6):
        if not count[i]: return 0
    return 30

def bsCalc():
    for i in range(2,7):
        if not count[i]: return 0
    return 30

def yacht():
    for i in range(1,7):
        if count[i]==5: return 50
    return 0
    
    

cmd=list(map(lambda x: x=='Y', input()))
number=list(map(int,input().split()))+[0]*2
answer=0
for i in range(1,7):
    number[3]=i
    for j in range(1,7):
        number[4]=j
        count=[0]*7
        for x in number:
            count[x]+=1
        answer=max(answer,calc())

print(answer)
