from collections import deque

dx=(-1,0,1,0)
dy=(0,1,0,-1)

def sol():
    q=deque()
    if board[0][1]=='L':
        q.append((0,1,2))
        visited[0][1][2]=1
    else:
        q.append((0,1,1))
        visited[0][1][1]=1
    if board[1][0]=='L':
        q.append((1,0,1))
        visited[1][0][1]=1
    while q:
        x,y,d = q.popleft()
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<2 and 0<=ny<n:
            if nx==1 and ny==n-1: return 'YES'
            if board[nx][ny]=='L':
                for nd in ((d+1)%4,(d-1)%4):
                    if not visited[nx][ny][nd]:
                        visited[nx][ny][nd]=1
                        q.append((nx,ny,nd))
            else:
                if not visited[nx][ny][d]:
                    visited[nx][ny][d]=1
                    q.append((nx,ny,d))
    
    return 'NO'

n=int(input())
board=[list(input()) for i in range(2)]
board[0][0]=0
board[-1][-1]=0
visited=[[[0]*4 for i in range(n)] for i in range(2)]

print(sol())