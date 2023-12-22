dx=((-1,0,1),(-1,-1,0))
dy=(0,-1,-1)

DIV=10**9+7

n,m=map(int,input().split())
board=[[0]*m for i in range(n)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    board[a-1][b-1]=-1
board[0][0]=1

for y in range(m):
    for x in range(n):
        if board[x][y]<0: continue
        for i in range(3):
            nx,ny=x+dx[1-y%2][i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]>=0:
                board[x][y]+=board[nx][ny]
        board[x][y]%=DIV
print(board[-1][-1])