import sys
input=sys.stdin.readline
from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    for _ in range(c):
        x,y=map(int,input().split())
        q.append((x-1,y-1))
        visited[x-1][y-1]=1
    cost=[]
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    if board[nx][ny]:
                        cost.append(board[nx][ny]*t)
        t+=1
    
    cost.sort()
    return cost[0]

n,m,r,c=map(int,input().split())

board=[[0]*m for i in range(n)]
for _ in range(r):
    x,y,z=map(int,input().split())
    board[x-1][y-1]=z
    
visited=[[0]*m for i in range(n)]

print(sol())
