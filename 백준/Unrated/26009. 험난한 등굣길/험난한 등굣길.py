import sys
input=sys.stdin.readline
from collections import deque


dx=(-1,1,0,0)
dy=(0,0,-1,1)

def block(x,y,d):
    nx,ny=x-d, y
    if 0<=nx<n and 0<=ny<m: board[nx][ny]=1
    for i in range(d):
        nx+=1
        ny+=1
        if 0<=nx<n and 0<=ny<m: board[nx][ny]=1
    for i in range(d):
        nx+=1
        ny-=1
        if 0<=nx<n and 0<=ny<m: board[nx][ny]=1
    for i in range(d):
        nx-=1
        ny-=1
        if 0<=nx<n and 0<=ny<m: board[nx][ny]=1
    for i in range(d):
        nx-=1
        ny+=1
        if 0<=nx<n and 0<=ny<m: board[nx][ny]=1
                                        
def sol():
    q=deque()
    q.append((0,0))
    visited=[[0]*m for i in range(n)]
    visited[0][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==n-1 and y==m-1: return ['YES',t]
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return ['NO']        

n,m=map(int,input().split())
board=[[0]*m for i in range(n)]
for _ in range(int(input())):
    x,y,d=map(int,input().split())
    block(x-1,y-1,d)
    
print(*sol(),sep='\n')
