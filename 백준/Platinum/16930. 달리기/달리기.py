from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)



def bfs():
    q=deque()
    q.append((x1-1,y1-1))
    visited[x1-1][y1-1]=0
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==x2 and y==y2: return t
            for i in range(4):
                nx,ny=x,y
                for j in range(k):
                    nx+=dx[i]
                    ny+=dy[i]
                    if not (0<=nx<n and 0<=ny<m) or board[nx][ny]=='#': break
                    elif visited[nx][ny]!=-1 and visited[nx][ny]<=visited[x][y]:break
                    elif visited[nx][ny]==-1:
                        q.append((nx,ny))
                        visited[nx][ny]=t+1
        t+=1            
    return -1

n,m,k=map(int,input().split())
board=[list(input()) for i in range(n)]
x1,y1,x2,y2=map(int,input().split())
x2-=1
y2-=1
visited=[[-1]*m for i in range(n)]
print(bfs())
