import sys
sys.setrecursionlimit(10**6)

dx=(0,0,-1,1)
dy=(1,-1,0,0)

def sol(x,y,d):
    #print(x,y,d)
    if not (0<x<=n and 0<y<=m):
        return visited[x][y]
    if board[x-1][y-1]==1: d=(d+2)%4
    if not visited[x][y][d]:
        nx,ny= x+dx[d], y+dy[d]
        visited[x][y][d]=sol(nx,ny,d)
    return visited[x][y][d]

n,m=map(int,input().split())
board=[]
board=[list(map(int,input().split())) for i in range(n)]
visited=[[[0]*4 for i in range(m+2)] for i in range(n+2)]

cnt=1
for i in range(1,n+1):
    visited[i][0]=cnt
    cnt+=1
for i in range(1,m+1):
    visited[n+1][i]=cnt
    cnt+=1
for i in range(n,0,-1):
    visited[i][m+1]=cnt
    cnt+=1
for i in range(m,0,-1):
    visited[0][i]=cnt
    cnt+=1

for i in range(1,n+1):
    print(sol(i,1,0),end=' ')
for i in range(1,m+1):
    print(sol(n,i,2),end=' ')
for i in range(n,0,-1):
    print(sol(i,m,1),end=' ')
for i in range(m,0,-1):
    print(sol(1,i,3),end=' ')

    