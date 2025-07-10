from collections import deque

def sol():
    if compare()==-1:
        newValue=calcLeft()
        for _ in range(3):expr.popleft()
        expr.appendleft(newValue)
    else:
        newValue=calcRight()
        for _ in range(3):expr.pop()
        expr.append(newValue)

def compare():
    leftPrior= 1 if expr[1] in '*/' else 0
    rightPrior= 1 if expr[-2] in '*/' else 0
    if leftPrior>rightPrior: return -1
    elif leftPrior<rightPrior: return 1

    if calcRight()>calcLeft(): return 1
    else: return -1

def divide(x,y):
    if x==0:return 0
    if x*y>0: return x//y
    a,b=divmod(x,y)
    if b: a+=1
    return a

def calcLeft():
    if expr[1]=='+': leftValue=expr[0]+expr[2]
    elif expr[1]=='-': leftValue=expr[0]-expr[2]
    elif expr[1]=='*': leftValue=expr[0]*expr[2]
    else: leftValue=divide(expr[0],expr[2])
    
    return leftValue

def calcRight():
    if expr[-2]=='+': rightValue=expr[-3]+expr[-1]
    elif expr[-2]=='-': rightValue=expr[-3]-expr[-1]
    elif expr[-2]=='*': rightValue=expr[-3]*expr[-1]
    else: rightValue=divide(expr[-3],expr[-1])

    return rightValue
    

ori=list(input())
expr=deque()
temp=[]
temp.append(ori[0])
for i in range(1,len(ori)):
    now=ori[i]
    if now in '+-*/':
        expr.append(int(''.join(temp)))
        expr.append(now)
        temp=[]
    else: temp.append(now)
expr.append(int(''.join(temp)))
    
while len(expr)>1: sol()

print(expr[0])