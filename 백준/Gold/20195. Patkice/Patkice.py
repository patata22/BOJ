from collections import deque

dx=(0,-1,1,0)
dy=(1,0,0,-1)
dd=('E','N','S','W')

def sol():
    q=deque()
    visited[sx][sy]=1
    for i in range(4):
        x,y=sx+dx[i],sy+dy[i]
        if 0<=x<n and 0<=y<m and board[x][y]!=-1:
            q.append((x,y,i))
            visited[x][y]=1
    while q:
        x,y,d=q.popleft()
        if x==ex and y==ey:
            print(':)')
            print(dd[d])
            return
        i=board[x][y]
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1 and not visited[nx][ny]:
            visited[nx][ny]=1
            q.append((nx,ny,d))
    print(':(')
    return
            

n,m=map(int,input().split())

board=[list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]=='o':sx,sy=i,j
        elif board[i][j]=='x':ex,ey=i,j
        elif board[i][j]=='^': board[i][j]=1
        elif board[i][j]=='v': board[i][j]=2
        elif board[i][j]=='<': board[i][j]=3
        elif board[i][j]=='>': board[i][j]=0
        elif board[i][j]=='.': board[i][j]=-1
visited=[[0]*m for i in range(n)]

sol()
