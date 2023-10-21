from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def bfs(i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='#' and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
visited=[[0]*m for i in range(n)]
answer=0
for i in range(n):
    for j in range(m):
        if board[i][j]=='#' and not visited[i][j]:
            answer+=1
            bfs(i,j)
print(answer)
            