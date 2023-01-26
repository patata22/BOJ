from collections import deque

dx=(-2,-3,-3,-2,2,3,3,2)
dy=(-3,-2,2,3,-3,-2,2,3)
dr=(((0,-1),(-1,-2)),((-1,0),(-2,-1)),((-1,0),(-2,1)),((0,1),(-1,2)),((0,-1),(1,-2)), ((1,0),(2,-1)),((1,0),(2,1)),((0,1),(1,2)))


def check(x,y,i):
    for dx,dy in dr[i]:
        nx,ny=x+dx,y+dy
        if nx==ex and ny==ey: return False
    return True
        
    

def sol():
    q=deque()
    visited=[[0]*9 for i in range(10)]
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            if x==ex and y==ey: return t
            for i in range(8):
                nx,ny= x+dx[i],y+dy[i]
                if 0<=nx<10 and 0<=ny<9 and not visited[nx][ny] and check(x,y,i):
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1

sx,sy=map(int,input().split())
ex,ey=map(int,input().split())

print(sol())
