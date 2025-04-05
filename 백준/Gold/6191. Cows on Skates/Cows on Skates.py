from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    n,m=map(int,input().split())
    board=[list(input()) for i in range(n)]
    q=deque()
    q.append((0,0))
    visited=[[-1]*m for i in range(n)]
    visited[0][0]=0
    while q:
        x,y=q.popleft()
        if x==n-1 and y==m-1: break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and visited[nx][ny]==-1:
                visited[nx][ny]=i
                q.append((nx,ny))

    x,y=n-1,m-1
    result=[]
    print(1,1)
    while not (x==0 and y==0):
        result.append((x+1,y+1))
        i=visited[x][y]
        x,y= x-dx[i],y-dy[i]

    for x in result[::-1]:  print(*x)
    
sol()