DIV=10**9+7

n=int(input())
dp=[[0]*3 for i in range(n)]
dp[0]=[1,1,1]
for i in range(1,n):
    dp[i][0]=sum(dp[i-1])%DIV
    dp[i][1]=sum(dp[i-1])%DIV
    dp[i][2]=(dp[i-1][0]+dp[i-1][1])%DIV
    
print(sum(dp[-1])%DIV)

