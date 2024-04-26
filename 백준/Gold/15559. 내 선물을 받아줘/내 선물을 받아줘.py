import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b: p[b]=a
    
def travel(x,y):
    while True:
        nx,ny=x,y
        visited[x][y]=1
        if board[x][y]=='N': nx-=1
        elif board[x][y]=='W': ny-=1
        elif board[x][y]=='E': ny+=1
        else: nx+=1
        union(x*m+y, nx*m+ny)
        if visited[nx][ny]: return
        x,y=nx,ny

n,m=map(int,input().split())
board=[list(input().rstrip()) for i in range(n)]
visited=[[0]*m for i in range(n)]
p=[-1]*(n*m)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            travel(i,j)

answer=0
for i in range(n*m):
    if p[i]<0:answer+=1
print(answer)
