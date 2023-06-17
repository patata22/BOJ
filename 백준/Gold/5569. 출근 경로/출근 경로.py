DIV=100000

n,m=map(int,input().split())

dp=[[[[0]*2 for i in range(2)] for i in range(m)] for i in range(n)]
dp[1][0][0][0]=1 #x,y, 0=북 1=동, 0=안돎, 1=돎
dp[0][1][1][0]=1
for i in range(n):
    for j in range(m):
        dp[i][j][0][0]+=sum(dp[i-1][j][0])%DIV
        dp[i][j][0][1]+=dp[i-1][j][1][0]%DIV
        dp[i][j][1][0]+=sum(dp[i][j-1][1])%DIV
        dp[i][j][1][1]+=dp[i][j-1][0][0]%DIV

print((sum(dp[-1][-1][0])+sum(dp[-1][-1][1]))%DIV)