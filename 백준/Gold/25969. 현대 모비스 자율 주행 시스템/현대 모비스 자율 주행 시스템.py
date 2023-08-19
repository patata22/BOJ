from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

DX=[]
DY=[]

def sol():
    q=deque()
    q.append((0,0,0,0))
    visited[0][0][0][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,k,p = q.popleft()
            if x==n-1 and y==m-1 and p: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=1 and not visited[nx][ny][k][p]:
                    if board[nx][ny]==2:
                        visited[nx][ny][k][1]=1
                        q.append((nx,ny,k,1))
                    else:
                        visited[nx][ny][k][p]=1
                        q.append((nx,ny,k,p))
            if k<K:
                for i in range(len(DX)):
                    nx,ny=x+DX[i],y+DY[i]
                    if 0<=nx<n and 0<=ny<m and board[nx][ny]!=1 and not visited[nx][ny][k+1][p]:
                        if board[nx][ny]==2:
                            visited[nx][ny][k+1][1]=1
                            q.append((nx,ny,k+1,1))
                        else:
                            visited[nx][ny][k+1][p]=1
                            q.append((nx,ny,k+1,p))                         
        t+=1
    return -1
            
n,m,K=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
for x in range(-2,3):
    temp = tuple(map(int,input().split()))
    for y in range(5):
        if not x and y==2: continue
        if temp[y]:
            DX.append(x)
            DY.append(y-2)

l=len(DX)
visited=[[[[0]*2 for i in range(K+1)] for j in range(m)] for i in range(n)]
print(sol())
