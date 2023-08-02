import sys
input=sys.stdin.readline

stack=[]

for _ in range(int(input())):
    x=list(map(int,input().split()))
    if x[0]==1: stack.append(x[1])
    elif x[0]==2:
        if stack: print(stack.pop())
        else: print(-1)
    elif x[0]==3: print(len(stack))
    elif x[0]==4: print(1-int(bool(stack)))
    else:
        if stack: print(stack[-1])
        else: print(-1)
        
