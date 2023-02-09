from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny= (x+dx[i])%n, (y+dy[i])%m
            if not board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]

answer=0

for i in range(n):
    for j in range(m):
        if not board[i][j] and not visited[i][j]:
            
            answer+=1
            visited[i][j]=1
            sol(i,j)

print(answer)