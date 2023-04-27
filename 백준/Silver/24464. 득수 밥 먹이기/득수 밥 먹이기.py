DIV=10**9+7
n=int(input())
dp=[[0]*5 for i in range(n)]
dp[0]=[1,1,1,1,1]
for i in range(1,n):
    dp[i][0]=(dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4])%DIV
    dp[i][1]=(dp[i-1][0]+dp[i-1][3]+dp[i-1][4])%DIV
    dp[i][2]=(dp[i-1][0]+dp[i-1][4])%DIV
    dp[i][3]=(dp[i-1][0]+dp[i-1][1])%DIV
    dp[i][4]=(dp[i-1][0]+dp[i-1][1]+dp[i-1][2])

print(sum(dp[-1])%DIV)