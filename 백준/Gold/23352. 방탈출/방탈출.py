from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(X,Y):
    global long,answer
    q=deque()
    q.append((X,Y))
    before=deque()
    visited=[[0]*m for i in range(n)]
    visited[X][Y]=1
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            before.append((x,y))
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        if q:
            before=deque()
            t+=1
        elif t>=long:
            temp=0
            for x,y in before:
                temp=max(temp, board[X][Y]+board[x][y])
            if t>long:
                long=t
                answer=temp
            elif t==long:
                answer=max(answer,temp)

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
answer=0
long=0
for i in range(n):
    for j in range(m):
        if board[i][j]:
            if 1<i<n-1 and board[i-1][j] and board[i+1][j]:continue
            if 1<j<m-1 and board[i][j-1] and board[i][j+1]:continue
            sol(i,j)
print(answer)