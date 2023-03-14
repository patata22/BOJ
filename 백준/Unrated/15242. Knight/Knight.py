from collections import deque

dx=(-1,-2,-2,-1,1,2,2,1)
dy=(-2,-1,1,2,-2,-1,1,2)

def change(x):
    return (ord(x[0])-97,int(x[1])-1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t
            for i in range(8):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<8 and 0<=ny<8 and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
visited=[[0]*8 for i in range(8)]
sx,sy=change(input())
ex,ey=change(input())

print(sol())