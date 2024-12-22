from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol1(x1,y1,x2,y2,x3,y3,x4,y4):
    q=deque()
    q.append((x1,y1))
    visited[x1][y1]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==x2 and y==y2: T=t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if (nx==x3 and ny==y3) or (nx==x4 and ny==y4): continue
                if 0<=nx<=n and 0<=ny<=m and not visited[nx][ny]:
                    visited[nx][ny]=1
                    prev[nx][ny]=(x,y)
                    q.append((nx,ny))
        t+=1
    x,y=x2,y2
    while x!=x1 or y!=y1:
        visited2[x][y]=1
        x,y=prev[x][y]
    return T

def sol2(x1,y1,x2,y2,x3,y3,x4,y4):
    q=deque()
    q.append((x3,y3))
    visited2[x1][y1]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==x4 and y==y4: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<=n and 0<=ny<=m and not visited2[nx][ny]:
                    visited2[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return float('inf')

m,n=map(int,input().split())

y1,x1=map(int,input().split())
y2,x2=map(int,input().split())
y3,x3=map(int,input().split())
y4,x4=map(int,input().split())
answer1=0
visited=[[0]*(m+1) for i in range(n+1)]
visited2=[[0]*(m+1) for i in range(n+1)]
prev=[[0]*(m+1) for i in range(n+1)]
answer1+=sol1(x1,y1,x2,y2,x3,y3,x4,y4)
answer1+=sol2(x1,y1,x2,y2,x3,y3,x4,y4)
answer2=0
visited=[[0]*(m+1) for i in range(n+1)]
visited2=[[0]*(m+1) for i in range(n+1)]
prev=[[0]*(m+1) for i in range(n+1)]
answer2+=sol1(x3,y3,x4,y4,x1,y1,x2,y2)
answer2+=sol2(x3,y3,x4,y4,x1,y1,x2,y2)
answer=min(answer1,answer2)
if answer==float('inf'): print('IMPOSSIBLE')
else:print(answer)
