def sol(start, now, cnt):
    global answer,gap
    if cnt==3:
        if m-now<gap:
            gap=m-now
            answer=now        
        return
    for i in range(start, n):
        if not used[i] and now+cards[i]<=m:
            used[i]=1
            sol(i+1,now+cards[i],cnt+1)
            used[i]=0
    

n,m=map(int,input().split())
cards=list(map(int,input().split()))
used=[0]*n
gap=float('inf')
answer=0
sol(0,0,0)
print(answer)
