n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
dp=[[[0]*3 for i in range(n)] for i in range(n)]
dp[0][1][0]=1
for x in range(n):
    for y in range(n):
        if board[x][y]==0:
            if 0<y:
                dp[x][y][0]+=dp[x][y-1][0]+dp[x][y-1][2]
            if 0<x:
                dp[x][y][1]+=dp[x-1][y][1]+dp[x-1][y][2]
            if 0<x and 0<y:
                if board[x-1][y]==0 and board[x][y-1]==0:
                    dp[x][y][2]+=sum(dp[x-1][y-1])
print(sum(dp[-1][-1]))