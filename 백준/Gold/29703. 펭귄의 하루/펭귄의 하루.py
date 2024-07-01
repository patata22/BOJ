from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy,0))
    visited[sx][sy][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,fish=q.popleft()
            if board[x][y]=='H' and fish: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny]=='D': continue
                    elif board[nx][ny]=='F':
                        if not visited[nx][ny][1]:
                            visited[nx][ny][1]=1
                            q.append((nx,ny,1))
                    else:
                        if not visited[nx][ny][fish]:
                            visited[nx][ny][fish]=1
                            q.append((nx,ny,fish))
                    
        t+=1
    return -1
            
n,m=map(int,input().split())

board=[list(input()) for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]=='S':
            board[i][j]='E'
            sx,sy=i,j
visited=[[[0]*2 for i in range(m)] for i in range(n)]
print(sol())
