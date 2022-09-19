def sol(day, now):
    global answer
    if day==n:
        answer+=1
        return
    for i in range(n):
        if not used[i] and now+weight[i]-k>=500:
            used[i]=1
            sol(day+1, now+weight[i]-k)
            used[i]=0
        

n,k=map(int,input().split())
weight=list(map(int,input().split()))
used=[0]*n
answer=0
sol(0,500)
print(answer)
