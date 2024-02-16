from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def travel(x,y,num):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    board[x][y]=num
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='X' and not visited[nx][ny]:
                visited[nx][ny]=1
                board[nx][ny]=num
                q.append((nx,ny))
def sol():
    q=deque()
    visited=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                q.append((i,j))
                visited[i][j]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]==2: return t-1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
visited=[[0]*m for i in range(n)]
num=1

for i in range(n):
    for j in range(m):
        if board[i][j]=='X':
            travel(i,j,num)
            num+=1
print(sol())
