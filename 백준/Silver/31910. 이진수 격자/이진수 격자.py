n=int(input())
dp=[list(map(int,input().split())) for i in range(n)]
for i in range(1,n):
    dp[0][i]+=dp[0][i-1]<<1
    dp[i][0]+=dp[i-1][0]<<1

for i in range(1,n):
    for j in range(1,n):
        dp[i][j]+=max(dp[i-1][j],dp[i][j-1])<<1
print(dp[-1][-1])