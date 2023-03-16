from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                sx,sy=i,j
            elif maps[i][j]=='E':
                ex,ey=i,j
            elif maps[i][j]=='L':
                lx,ly=i,j
                
    q=deque()
    q.append((sx,sy,0))
    visited=[[[0]*2 for i in range(m)] for i in range(n)]
    visited[sx][sy][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,z = q.popleft()
            if x==ex and y==ey and z: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny]!='X' and not visited[nx][ny][z]:
                    visited[nx][ny][z]=1
                    if nx==lx and ny==ly:
                        q.append((nx,ny,1))
                    else: q.append((nx,ny,z))
        t+=1
    return -1