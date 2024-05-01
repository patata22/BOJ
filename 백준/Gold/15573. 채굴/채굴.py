from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def bfs(mid):
    q=deque()
    visited=[[0]*m for i in range(n)]
    cnt=0
    for i in range(n):
        for j in (0,m-1):
            if not visited[i][j] and board[i][j]<=mid:
                visited[i][j]=1
                q.append((i,j))
                cnt+=1
    for j in range(m):
        if not visited[0][j] and board[0][j]<=mid:
                visited[0][j]=1
                q.append((0,j))
                cnt+=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]<=mid and not visited[nx][ny]:
                visited[nx][ny]=1
                cnt+=1
                q.append((nx,ny))

    if cnt>=k: return True
    else: return False

def sol():
    l=0
    r=10**6
    while l+1<r:
        mid=(l+r)//2
        if bfs(mid): r=mid
        else: l=mid
    return r

n,m,k=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
print(sol())
