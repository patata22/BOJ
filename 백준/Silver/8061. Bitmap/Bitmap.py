from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    n,m=map(int,input().split())
    board=[list(map(int,input())) for i in range(n)]
    visited=[[-1]*m for i in range(n)]
    q=deque()
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                visited[i][j]=0
                q.append((i,j))
    t=1
    while q:
        for __ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]<0:
                    visited[nx][ny]=t
                    q.append((nx,ny))
        t+=1
    for i in range(n):print(*visited[i])

sol()
