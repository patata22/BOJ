n,k=map(int,input().split())

score=list(map(int,input().split()))
cost=list(map(int,input().split()))

dp=[[-float('inf')]*101 for i in range(n+1)]
dp[0][100]=0
for i in range(n):
    for j in range(101):
        if dp[i][j]<0: continue
        nxt=min(j+k,100)
        dp[i+1][nxt]=max(dp[i+1][nxt],dp[i][j])
        nxt-=cost[i]
        if nxt<0: continue
        dp[i+1][nxt]=max(dp[i+1][nxt],dp[i][j]+score[i])

answer=max(dp[-1])
if answer==-float('inf'): print(0)
else: print(answer)
