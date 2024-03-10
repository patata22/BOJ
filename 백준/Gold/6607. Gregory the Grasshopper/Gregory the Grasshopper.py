from collections import deque

dx=(-1,-2,-2,-1,1,2,2,1)
dy=(-2,-1,1,2,-2,-1,1,2)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t
            for i in range(8):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return 'impossible'


while True:
    try:
        n,m,sx,sy,ex,ey=map(lambda x: int(x)-1,input().split())
        n+=1
        m+=1
        print(sol())
    except:
        break
