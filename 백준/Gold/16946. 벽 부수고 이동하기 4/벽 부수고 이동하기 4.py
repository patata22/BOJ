from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def travel(x,y,unused):
    q=deque()
    q.append((x,y))
    board[x][y]=unused
    total=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not board[nx][ny]:
                total+=1
                board[nx][ny]=unused
                q.append((nx,ny))
    return total

def change(x,y):
    total=1
    visited=set()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]>1 and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            total+=moveCount[board[nx][ny]]
    return total%10            
            
            

n,m=map(int,input().split())
board=[list(map(int,list(input().rstrip()))) for i in range(n)]
moveCount={}
unused=2
for x in range(n):
    for y in range(m):
        if not board[x][y]:
            moveCount[unused]=travel(x,y,unused)
            unused+=1

answer=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]==1: answer[i][j]=change(i,j)

for i in range(n):
    print(*answer[i],sep='')
