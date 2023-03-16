from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    
    q=deque()
    q.append((0,0))
    visited=[[0]*m for i in range(n)]
    visited[0][0]=1
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==n-1 and y==m-1: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1