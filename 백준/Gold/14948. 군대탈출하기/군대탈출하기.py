from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    l=board[0][0]-1
    r=10**9
    while l+1<r:
        mid=(l+r)//2
        result=travel(mid)
        if travel(mid):r=mid
        else: l=mid
    return r

def travel(mid):
    q=deque()
    q.append((0,0,1))
    level=board[0][0]
    visited=[[[0]*2 for i in range(m)] for i in range(n)]
    visited[0][0][1]=1
    while q:
        x,y,jump=q.popleft()
        if x==n-1 and y==m-1: return True
        if jump:
            for i in range(4):
                nx,ny=x+2*dx[i],y+2*dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]<=mid and not visited[nx][ny][0]:
                    visited[nx][ny][0]=1
                    q.append((nx,ny,0))
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]<=mid and not visited[nx][ny][jump]:
                visited[nx][ny][jump]=1
                q.append((nx,ny,jump))

    return False

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
print(sol())