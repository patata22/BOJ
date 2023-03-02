import sys
input=sys.stdin.readline

dx=(-1,0)
dy=(0,-1)

n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
dp=[[0]*(m+1) for i in range(n+1)]

for x in range(1,n+1):
    for y in range(1,m+1):
        for d in range(2):
            nx,ny=x+dx[d], y+dy[d]
            if 0<nx<=n and 0<ny<=m:
                dp[x][y]+=dp[nx][ny]
        dp[x][y]-=dp[x-1][y-1]
        dp[x][y]+=board[x-1][y-1]

            
for _ in range(int(input())):
    a,b,c,d= map(int,input().split())
    a-=1
    b-=1
    print(dp[c][d]-dp[a][d]-dp[c][b]+dp[a][b])
