n,m=map(int,input().split())
charms=[tuple(map(int,input().split())) for i in range(n)]
dp=[[0]*(m+1) for i in range(2)]
for i in range(n):
    w,v=charms[i]
    for j in range(m+1):
        if j<w: dp[1][j]=dp[0][j]
        else:
            dp[1][j]=max(dp[0][j],dp[0][j-w]+v)
    dp[0]=dp[1]
    dp[1]=[0]*(m+1)
print(dp[0][-1])
