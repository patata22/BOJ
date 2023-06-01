n=int(input())
board=[tuple(map(int,input().split())) for i in range(n)]
dp=[[[0]*3 for i in range(n)] for i in range(n)]
dp[0][1][0]=1
for i in range(n):
    for j in range(n):
        if board[i][j]==0:
            dp[i][j][0]+=dp[i][j-1][0]+dp[i][j-1][2]
            dp[i][j][1]+=dp[i-1][j][1]+dp[i-1][j][2]
            if i>0 and j>0 and board[i-1][j]==0 and board[i][j-1]==0:
                dp[i][j][2]+=sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))
            
