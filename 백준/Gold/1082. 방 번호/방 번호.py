n=int(input())
price=tuple(map(int,input().split()))
m=int(input())
dp=[[0]*(m+1) for i in range(n)]

for i in range(n-1,-1,-1):
    p=price[i]
    for j in range(m+1):
        dp[i][j]=dp[(i+1)%n][j]
        if j>=p:
            dp[i][j]=max(dp[i][j],dp[i][j-p]*10+i,dp[(i+1)%n][j-p]*10+i)
print(dp[0][-1])