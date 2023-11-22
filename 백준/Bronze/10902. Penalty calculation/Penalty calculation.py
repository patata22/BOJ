S=[]
time=[]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    S.append(b)
    time.append((a,b))
S=max(S)
for i in range(n):
    t,s=time[i]
    if s==S:
        if not s:print(0)
        else:print(i*20+t)
        break
        
