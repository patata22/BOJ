from collections import deque
import sys
input=sys.stdin.readline
dx=(-1,1,0,0)
dy=(0,0,1,-1)
change4={1:2, 2:1, 0:3, 3:0}

def travel(x,y,i):
    nx,ny=x+dx[i],y+dy[i]
    while 0<=nx<n and 0<=ny<m:
        if visited[nx][ny][i]:return
        visited[nx][ny][i]=1
        wind[nx][ny]=1
        if board[nx][ny]==1 and i//2: return
        elif board[nx][ny]==2 and not i//2: return
        elif board[nx][ny]==3: i=(i+2)%4
        elif board[nx][ny]==4: i=change4[i]
        nx+=dx[i]
        ny+=dy[i]
        
n,m=map(int,input().split())
board=[]
air=[]
for i in range(n):
    temp=tuple(map(int,input().split()))
    for j in range(m):
        if temp[j]==9:
            air.append((i,j))
    board.append(temp)
visited=[[[0]*4 for i in range(m)] for i in range(n)]
wind=[[0]*m for i in range(n)]

for x, y in air:
    wind[x][y]=1
    for i in range(4):
        visited[x][y][i]=1
        travel(x,y,i)

answer=0
for i in range(n):
    for j in range(m):
        answer+=wind[i][j]
print(answer)
