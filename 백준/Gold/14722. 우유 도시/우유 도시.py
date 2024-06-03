n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
dp=[[[-float('inf')]*3 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]==0: dp[i][j][0]=1

for i in range(1,n):
    for k in range(3):
        if board[0][i]==k:dp[0][i][k]=max(dp[0][i][k],dp[0][i-1][k],dp[0][i-1][(k-1)%3]+1)
        else:dp[0][i][k]=max(dp[0][i][k],dp[0][i-1][k])
        if board[i][0]==k:dp[i][0][k]=max(dp[i][0][k],dp[i-1][0][k],dp[i-1][0][(k-1)%3]+1)
        else: dp[i][0][k]=max(dp[i][0][k],dp[i-1][0][k])
        
for i in range(1,n):
    for j in range(1,n):
        for k in range(3):
            if board[i][j]==k:dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k],dp[i][j-1][k],dp[i-1][j][(k-1)%3]+1, dp[i][j-1][(k-1)%3]+1)
            else: dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k], dp[i][j-1][k])

if max(dp[-1][-1])==-float('inf'):print(0)
else: print(max(dp[-1][-1]))
