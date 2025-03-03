from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:return 'YES'
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==board[x][y] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=1                    
    return 'NO'
                    
for tt in range(int(input())):
    m,n,sy,sx,ey,ex=map(int,input().split())
    board=[list(input()) for i in range(n)][::-1]
    sx-=1
    sy-=1
    ex-=1
    ey-=1
    print(sol())