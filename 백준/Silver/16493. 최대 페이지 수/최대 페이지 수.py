n,m=map(int,input().split())
chapter = [tuple(map(int,input().split())) for i in range(m)]

dp=[[0]*(n+1) for i in range(m+1)]
for i in range(1,m+1):
    day,page=chapter[i-1]
    for j in range(1,n+1):
        if day>j:dp[i][j]=dp[i-1][j]
        else: dp[i][j]=max(dp[i-1][j],dp[i-1][j-day]+page)
print(max(dp[-1]))
                                

