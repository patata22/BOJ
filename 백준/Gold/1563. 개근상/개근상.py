DIV=1000000

n=int(input())
dp=[[[0]*3 for i in range(2)] for i in range(n)]
dp[0][0][0]=1
dp[0][1][0]=1
dp[0][0][1]=1

for i in range(1,n):
    
    dp[i][0][0]+=sum(dp[i-1][0])%DIV
    dp[i][1][0]+=sum(dp[i-1][1])%DIV
    
    dp[i][0][1]+=dp[i-1][0][0]%DIV
    dp[i][1][1]+=dp[i-1][1][0]%DIV
    dp[i][0][2]+=dp[i-1][0][1]%DIV
    dp[i][1][2]+=dp[i-1][1][1]%DIV
    
    dp[i][1][0]+=sum(dp[i-1][0])%DIV

print((sum(dp[-1][0])+sum(dp[-1][1]))%DIV)