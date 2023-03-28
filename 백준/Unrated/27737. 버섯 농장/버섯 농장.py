from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    global m
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    count=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                count+=1
                q.append((nx,ny))

    m-=count//k
    if count%k:m-=1
    return



n,m,k=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
visited=[[0]*n for i in range(n)]
flag=False
for i in range(n):
    for j in range(n):
        if not board[i][j] and not visited[i][j]:
            flag=True
            sol(i,j)

if not flag or m<0: print('IMPOSSIBLE')
else:print('POSSIBLE',m,sep='\n')
