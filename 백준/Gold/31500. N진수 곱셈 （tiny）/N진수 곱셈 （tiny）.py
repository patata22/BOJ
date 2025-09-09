def change(x):
    return ord(x)-33

def parse(x):
    neg=False
    base=1
    result=0
    while x:
        now=x.pop()
        if now=='~': neg=True
        else:
            result+=base*change(now)
            base*=n
    if neg: result*=-1
    return result

def sol(x):
    neg=x<0
    result=[]
    if neg: x=-x
    while x:
        result.append(chr(x%n+33))
        x//=n
    if neg:result.append('~')

    return ''.join(result[::-1])

def sol2(x):
    m=-n
    result=[]
    while x:
        temp=x%m
        x=(x-temp)//n
        result.append(chr(temp+33))
    return ''.join(result[::-1])

n=int(input())

A=list(input())
B=list(input())

a=parse(A)
b=parse(B)

if not a*b: print('!')
elif n>=0:print(sol(a*b))
else: print(sol2(a*b))
