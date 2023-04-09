from collections import deque
dx=(-1,1,0,0)
dy=(0,0,-1,1)
d={'U':0, 'D':1,'L':2,'R':3}

def fill(x,y,target,num):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    board[x][y]=num
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==target and not visited[nx][ny]:
                board[nx][ny]=num
                visited[nx][ny]=1
                q.append((nx,ny))
                

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
visited=[[0]*m for i in range(n)]
ward=set()
num=0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            num+=1
            fill(i,j,board[i][j],num)

x,y=map(int,input().split())
x-=1
y-=1


for cmd in input():
    if cmd=='W':
        ward.add(board[x][y])
    else:
        x,y=x+dx[d[cmd]],y+dy[d[cmd]]
answer=[['#']*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] in ward: answer[i][j]='.'
answer[x][y]='.'
for i in range(4):
    nx,ny=x+dx[i],y+dy[i]
    if 0<=nx<n and 0<=ny<m: answer[nx][ny]='.'


for i in range(n):
    print(*answer[i],sep='')
