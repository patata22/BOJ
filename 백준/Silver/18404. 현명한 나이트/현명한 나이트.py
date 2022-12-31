from collections import deque

dx=(-1,-2,-2,-1,1,2,2,1)
dy=(-2,-1,1,2,-2,-1,1,2)

def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y= q.popleft()
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if 0<nx<=n and 0<ny<=n and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    if board[nx][ny]: answer[board[nx][ny]-1]=t+1
        t+=1
    
n,m =map(int,input().split())
board = [[0]*(n+1) for i in range(n+1)]
visited=[[0]*(n+1) for i in range(n+1)]
answer=[0]*m

sx,sy = map(int,input().split())

for i in range(1,m+1):
    x,y=map(int,input().split())
    board[x][y]=i

sol()
print(*answer)
