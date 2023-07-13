def travel(now, visited):
    if dp[now][visited]!=-1: return dp[now][visited]
    if visited==finished:
        if cost[now][0]!=0:
            return cost[now][0]
    temp=float('inf')
    for i in range(n):
        if visited&(1<<i) or not cost[now][i]: continue
        temp=min(temp,travel(i,visited|(1<<i))+cost[now][i])
    dp[now][visited]=temp
    return dp[now][visited]
            

n=int(input())
finished=(1<<n)-1
cost=[tuple(map(int,input().split())) for i in range(n)]

dp=[[-1]*(1<<n) for i in range(n)]

answer=travel(0,1)
print(answer)
