from collections import deque

dx=(-1,0,1,0)
dy=(0,-1,0,1)


def sol():
    q=deque()
    for i in range(4):
        nx,ny=sx+dx[i], sy+dy[i]
        if 0<=nx<n and 0<=ny<m and 0<=board[nx][ny]<=k:
            visited[nx][ny][i]=1
            q.append((nx,ny,(i+2)%4))
    t=1
    while q:
        for _ in range(len(q)):
            x,y,D= q.popleft()
            if x==ex and y==ey: return t
            ox,oy=x+dx[D],y+dy[D]
            for d in range(4):
                if d==D: continue
                nx,ny=x+dx[d],y+dy[d]
                if 0<=nx<n and 0<=ny<m and 0<=board[nx][ny]<=k-board[ox][oy]-board[x][y] and not visited[nx][ny][d]:
                    visited[nx][ny][d]=1
                    q.append((nx,ny,(d+2)%4))

            
        t+=1
    return -1
            
n,m,k=map(int,input().split())
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='S':
            sx,sy=i,j
            x[j]=0
        elif x[j]=='H':
            ex,ey=i,j
            x[j]=0
        elif x[j]=='X':
            x[j]=-1
    board.append(list(map(int,x)))

visited=[[[0]*4 for i in range(m)] for i in range(n)]

print(sol())