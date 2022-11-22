DIV = 10**9 + 9
n=int(input())
dp= [[0]*3 for i in range(n+1)]
dp[1][0]=0
dp[1][1]=1
dp[1][2]=1
for i in range(2,n+1):
    for j in range(3):
        dp[i][j] = (dp[i-1][0]%DIV + dp[i-1][1]%DIV + dp[i-1][2]%DIV)%DIV
    
print(dp[-1][0])
