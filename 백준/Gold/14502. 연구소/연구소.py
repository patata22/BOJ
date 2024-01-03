from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def spread():
    q=deque()
    visited=[[0]*m for i in range(n)]
    for x,y in germ:
        visited[x][y]==1
        q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny))
    safe=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0 and visited[i][j]==0:
                safe+=1
    return safe


def choice(count,x):
    global answer
    if count==3:
        answer= max(answer,spread())
        return
    for i in range(x,len(space)):
        board[space[i][0]][space[i][1]]=1
        choice(count+1,i+1)
        board[space[i][0]][space[i][1]]=0
            
                

n,m=map(int,input().split())
board=[]
germ=[]
space=[]
answer=0
for i in range(n):
    x=list(map(int,input().split()))
    for j in range(m):
        if x[j]==2:germ.append((i,j))
        elif x[j]==0:space.append((i,j))
    board.append(x)
choice(0,0)
print(answer)
