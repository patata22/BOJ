from collections import deque

dx=(1,0)
dy=(0,1)
n=int(input())
board=[list(input()) for i in range(n)]
visited=[[0]*n for i in range(n)]

answer='No'
q=deque()
q.append((0,0))
while q:
    x,y=q.popleft()
    if x==n-1 and y==n-1: answer='Yes'
    for i in range(2):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny]=='.' and not visited[nx][ny]:
            visited[nx][ny]=1
            q.append((nx,ny))
    
print(answer)

