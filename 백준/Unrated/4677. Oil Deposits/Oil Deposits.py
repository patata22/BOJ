from collections import deque

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def sol(i,j):
    q=deque()
    q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='@' and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

while True:
    n,m=map(int,input().split())
    if not n: break
    board=[list(input()) for i in range(n)]
    visited=[[0]*m for i in range(n)]
    answer=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='@' and not visited[i][j]:
                answer+=1
                visited[i][j]=1
                sol(i,j)
    print(answer)
