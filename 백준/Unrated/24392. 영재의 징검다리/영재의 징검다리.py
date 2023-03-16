DIV=1000000007
dy=(-1,0,1)

n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
dp=[[0]*m for i in range(n)]
dp[0]=board[0]

for x in range(n-1):
    for y in range(m):
        if board[x][y]:
            for i in range(3):
                ny=y+dy[i]
                if 0<=ny<m and board[x+1][ny]:
             #       print(x,ny)
                    dp[x+1][ny]+=dp[x][y]
            
print(sum(dp[-1])%DIV)