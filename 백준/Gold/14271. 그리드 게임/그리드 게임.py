from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
visited=set()
q=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            q.append((i,j))
            visited.add((i,j))
k=int(input())
t=0
while t<k:
    for _ in range(len(q)):
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if (nx,ny) not in visited:
                q.append((nx,ny))
                visited.add((nx,ny))
    t+=1
print(len(visited))
    