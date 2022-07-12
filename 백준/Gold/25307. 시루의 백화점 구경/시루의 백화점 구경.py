from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def mane():
    t=0
    while t<k:
        for _ in range(len(stop)):
            x,y=stop.popleft()
            for i in range(4):
                nx,ny=x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    visited[nx][ny]=1
                    stop.append((nx,ny))
        t+=1

def sol():
    q=deque()
    q.append(start)
    visited[start[0]][start[1]]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]==2: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny] in (0,2) and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1
    
    

n,m,k=map(int,input().split())

board=[]
stop=deque()
for i in range(n):
    x=list(map(int,input().split()))
    for j in range(m):
        if x[j]==4: start=(i,j)
        elif x[j]==3: stop.append((i,j))
    board.append(x)
visited = [[0]*m for i in range(n)]
mane()
print(sol())