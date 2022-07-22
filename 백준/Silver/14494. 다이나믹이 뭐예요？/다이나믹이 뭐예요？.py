dx=(-1,0,-1)
dy=(0,-1,-1)
DIV=10**9+7

n,m=map(int,input().split())

dp=[[0]*m for i in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(m):
        for d in range(3):
            nx,ny=i+dx[d],j+dy[d]
            if 0<=nx<n and 0<=ny<m:
                dp[i][j]+=dp[nx][ny]
        dp[i][j]%=DIV
print(dp[-1][-1])
            
