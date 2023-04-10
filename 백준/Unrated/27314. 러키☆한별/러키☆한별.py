from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    q=deque()
    q.append((x,y))
    visited=[[0]*m for i in range(n)]
    visited[x][y]=1
    finished=False
    count=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]=='H': finished=True
            elif board[x][y]=='P': count+=1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!='X' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        if finished: return count
    return 0

n,m=map(int,input().split())

board=[]
start=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='H':
            ex,ey=i,j
        elif x[j]=='#':
            start.append((i,j))
    board.append(x)

answer=0
for x,y in start:
    answer=max(answer,sol(x,y))
print(answer)
