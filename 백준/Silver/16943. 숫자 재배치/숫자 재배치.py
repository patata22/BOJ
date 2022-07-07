def sol(cnt):
    global answer
    if cnt==n:
        temp=int(''.join(number))
        if temp<b:
            answer=max(answer,int(''.join(number)))
        return
    for i in range(n):
        if not used[i]:
            if cnt==0 and a[i]=='0':continue
            used[i]=1
            number.append(a[i])
            sol(cnt+1)
            number.pop()
            used[i]=0
                    
a,b=input().split()
a=list(a)
b=int(b)
n=len(a)
                   
answer=-1
used=[0]*n
number=[]

sol(0)
print(answer)
