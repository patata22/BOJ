from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(sx,sy,ex,ey):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t
            for d in range(4):
                nx,ny=x+dx[d],y+dy[d]
                if moveable(nx,ny,d) and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1

def moveable(nx,ny,d):
    if not (0<nx<=n-a+1 and 0<ny<=m-b+1 and board[nx][ny]):
        return False

    
    if d ==0:
        for i in range(ny, ny+b):
            if not board[nx][i]: return False
    elif d==1:
        for i in range(ny,ny+b):
            if not board[nx+a-1][i]: return False
    elif d==2:
        for i in range(nx,nx+a):
            if not board[i][ny]: return False
    elif d==3:
        for i in range(nx,nx+a):
            if not board[i][ny+b-1]: return False
    return True
        

n,m,a,b,k=map(int,input().split())
board=[[1]*(m+1) for i in range(n+1)]
visited=[[0]*(m+1) for i in range(n+1)]

for _ in range(k):
    x,y=map(int,input().split())
    board[x][y]=0

sx,sy=map(int,input().split())
ex,ey=map(int,input().split())

start=True
for i in range(sx,sx+a):
    for j in range(sy,sy+b):
        if not board[i][j]:
            start=False
if not start: print(-1)
else: print(sol(sx,sy,ex,ey))
