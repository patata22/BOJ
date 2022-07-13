from collections import deque

dx=(-1,-2,-2,-1,1,2,2,1)
dy=(-2,-1,1,2,-2,-1,1,2)

def move(X,Y,T):
    q=deque()
    q.append((X,Y))
    visited=[[float('inf')]*m for i in range(n)]
    t=T
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(8):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==float('inf'):
                    visited[nx][ny]=t//T
                    q.append((nx,ny))
        t+=1
    visited[X][Y]=0
    return visited
        

n,m=map(int,input().split())
board=[]
horse=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]!='.':
            horse.append((i,j,int(x[j])))
            x[j]='.'
    board.append(x)

distance=[[0]*m for i in range(n)]
for x,y,t in horse:
    temp=move(x,y,t)
    for i in range(n):
        for j in range(m):
            distance[i][j]+=temp[i][j]            

answer=float('inf')


for i in range(n):
    for j in range(m):
        answer=min(distance[i][j],answer)
print(-1) if answer==float('inf') else print(answer)
