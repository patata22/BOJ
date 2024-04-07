from collections import deque

dx=(1,0)
dy=(0,1)

def sol():
    q=deque()
    q.append((0,0))
    visited=[[0]*m for i in range(n)]
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

    print('Yes') if visited[-1][-1] else print('No')

m,n=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]

sol()
