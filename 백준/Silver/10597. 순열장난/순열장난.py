def sol(depth):
    global flag
    if flag: return
    if depth==n:
        flag=True
        print(*answer[::-1])
        return
    temp=x[-1]
    if temp and not used[temp]:
        x.pop()
        used[temp]=1
        answer.append(temp)
        sol(depth+1)
        answer.pop()
        used[temp]=0
        x.append(temp)
    if len(x)>1:
        temp = 10*x[-2]+x[-1]
        if 10<=temp<=n and not used[temp]:
            x.pop()
            x.pop()
            used[temp]=1
            answer.append(temp)
            sol(depth+1)
            answer.pop()
            used[temp]=0
            x.append(temp//10)
            x.append(temp%10)
            
            
x=list(map(int,list(input())))
if len(x)<10: n=len(x)
else: n= 9+(len(x)-9)//2
answer=[]
used=[0]*(n+1)
flag=False

sol(0)
