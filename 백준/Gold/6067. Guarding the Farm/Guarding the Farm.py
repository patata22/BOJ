from collections import deque

dx=(-1,1,0,0,-1,-1,1,1)
dy=(0,0,-1,1,-1,1,-1,1)

def sol(X,Y):
    q=deque()
    q.append((X,Y))
    visited[X][Y]=1
    now=board[X][Y]
    top=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]>now: top=0
                elif board[nx][ny]==now and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                
    if top: return 1
    return 0
    

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]
answer=0

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            answer+=sol(x,y)

print(answer)