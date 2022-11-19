from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=(-1,-1)
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx,ny= x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny]:
                visited[nx][ny]=(x,y)
                q.append((nx,ny))
                

n,m=map(int,input().split())
board= [list(input()) for i in range(n)]
visited= [[0]*m for i in range(n)]
goal=[]
for i in range(m):
    if board[0][i]=='.': goal.append((0,i))
    if board[n-1][i]=='.': goal.append((n-1,i))
for i in range(n):
    if board[i][0]=='.': goal.append((i,0))
    if board[i][m-1]=='.': goal.append((i,m-1))
sx,sy=goal[0]
ex,ey=goal[1]

sol()
for i in range(n):
    for j in range(m):
        if board[i][j]=='.':board[i][j]='@'
x,y=ex,ey
while x!=-1 and y!=-1:
    board[x][y]='.'
    x,y=visited[x][y]
for i in range(n):
    print(*board[i],sep='')
