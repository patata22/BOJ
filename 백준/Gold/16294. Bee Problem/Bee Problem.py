from collections import deque

dox=(-1,-1,0,0,1,1)
doy=(0,1,1,-1,1,0)
dex=(-1,-1,0,0,1,1)
dey=(-1,0,-1,1,-1,0)

def parse(x):
    if x=='.':return 0
    return 1

def bfs(x,y):
    visited[x][y]=1
    q=deque()
    q.append((x,y))
    cnt=1
    while q:
        x,y=q.popleft()
        if x%2==0:dx,dy=dex,dey
        else: dx,dy=dox,doy
        for i in range(6):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny]=1
                cnt+=1
                q.append((nx,ny))
    return cnt
                    
h,n,m=map(int,input().split())

board=[list(map(parse,input().strip().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]
space=[]
answer=0
for i in range(n):
    for j in range(m):
        if board[i][j]==0 and not visited[i][j]:
            space.append(bfs(i,j))
space.sort()
while h>0:
    answer+=1
    h-=space.pop()

print(answer)