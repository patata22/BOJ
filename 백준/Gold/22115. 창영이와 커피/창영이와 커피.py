n,k=map(int,input().split())
coffee=tuple(map(int,input().split()))

dp=[[float('inf')]*(k+1) for i in range(n)]
dp[0][0]=0
if coffee[0]<=k:
    dp[0][coffee[0]]=1
for i in range(1,n):
    co=coffee[i]
    for j in range(k+1):
        if j>=co: dp[i][j]=min(dp[i-1][j],dp[i-1][j-co]+1)
        else:dp[i][j]=min(dp[i][j],dp[i-1][j])
if dp[-1][-1]==float('inf'):print(-1)
else:print(dp[-1][-1])
       