from collections import deque

dx=(-1,-2,-2,-1,1,2,2,1)
dy=(-2,-1,1,2,-2,-1,1,2)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*9 for i in range(9)]
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t
            for i in range(8):
                nx,ny= x+dx[i],y+dy[i]
                if 0<nx<=8 and 0<ny<=8 and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
        
            


sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
print(sol())            
    
