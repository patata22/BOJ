from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((0,0))
    visited.add((0,0))
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==X and y==Y: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if abs(nx)<=500 and abs(ny)<=500 and ((nx,ny)) not in visited and ((nx,ny)) not in wet:
                    visited.add((nx,ny))
                    q.append((nx,ny))
        t+=1
    
    
    

X,Y,n=map(int,input().split())
wet=set()
visited=set()
for _ in range(n):
    wet.add(tuple(map(int,input().split())))
print(sol())
