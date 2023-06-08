c,n=map(int,input().split())
dp=[[0]*(1101) for i in range(n)]
city=[tuple(map(int,input().split())) for i in range(n)]
#dp[n][c]=n번째 도시까지 고려했을 때 C명 확보하기 위한 최소비용

for i in range(n):
    cost,guest=city[i]
    for j in range(1,1101):
        dp[i][j]=dp[i][j-guest]+cost


for i in range(1,n):
    cost,guest=city[i]
    for j in range(1101):
        dp[i][j]=min(dp[i][j],dp[i-1][j])
        if j>=guest:
            dp[i][j]=min(dp[i][j],dp[i-1][j-guest]+cost,dp[i][j-guest]+cost)
            
print(min(dp[-1][c:]))
