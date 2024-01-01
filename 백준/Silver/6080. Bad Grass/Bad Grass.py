from collections import deque

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def sol(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]

answer=0
for x in range(n):
    for y in range(m):
        if board[x][y] and not visited[x][y]:
            answer+=1
            sol(x,y)
print(answer)
