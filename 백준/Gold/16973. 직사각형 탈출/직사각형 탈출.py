from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def check(x,y):
    if not 0<x<=n or not 0<y<=m or visited[x][y]: return False
    if not 0<x+h-1<=n or not 0<y+w-1<=m: return False
    return board[x+h-1][y+w-1]-board[x+h-1][y-1]-board[x-1][y+w-1]+board[x-1][y-1]==0
def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if check(nx,ny):
                    visited[nx][ny]=1
                    q.append((nx,ny))

        t+=1
    return -1
        
n,m=map(int,input().split())
board=[[0]*(m+1)]
for _ in range(n):
    board.append([0]+list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,m+1):
        board[i][j]+=board[i][j-1]
for j in range(1,m+1):
    for i in range(1,n+1):
        board[i][j]+=board[i-1][j]

visited=[[0]*(m+1) for i in range(n+1)]
h,w,sx,sy,ex,ey= map(int,input().split())
print(sol())