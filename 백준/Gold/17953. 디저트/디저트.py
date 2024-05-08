n,m=map(int,input().split())

dessert=[tuple(map(int,input().split())) for i in range(m)]

dp=[[0]*m for i in range(n)]
for j in range(m):
    dp[0][j]=dessert[j][0]

for i in range(1,n):
    for j in range(m):
        for k in range(m):
            if j==k:
                dp[i][j]=max(dp[i][j],dp[i-1][k]+dessert[k][i]//2)
            else:
                dp[i][j]=max(dp[i][j],dp[i-1][k]+dessert[j][i])
print(max(dp[-1]))
