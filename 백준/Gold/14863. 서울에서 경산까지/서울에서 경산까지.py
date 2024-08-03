n,K=map(int,input().split())
dp=[[-1]*(K+1) for i in range(n+1)]
dp[0][0]=0
for i in range(n):
    wt,wm,bt,bm = map(int,input().split())
    for j in range(K+1):
        if dp[i][j]==-1: continue
        if j+wt<=K: dp[i+1][j+wt]=max(dp[i+1][j+wt],dp[i][j]+wm)
        if j+bt<=K: dp[i+1][j+bt]=max(dp[i+1][j+bt],dp[i][j]+bm)

print(max(dp[-1]))
