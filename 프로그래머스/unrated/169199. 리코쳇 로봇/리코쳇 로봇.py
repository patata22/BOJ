from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(board):
    n=len(board)
    m=len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R': sx,sy=i,j
            elif board[i][j]=='G': ex,ey=i,j
    
    q=deque()
    q.append((sx,sy))
    visited=[[[0]*4 for i in range(m)] for i in range(n)]
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t
            for i in range(4):
                nx,ny=x,y
                if not visited[nx][ny][i]:
                    visited[nx][ny][i]=1
                    while 0<=nx+dx[i]<n and 0<=ny+dy[i]<m and board[nx+dx[i]][ny+dy[i]]!='D':
                        visited[nx][ny][i]=1                       
                        nx+=dx[i]
                        ny+=dy[i]
                    q.append((nx,ny))
            
        t+=1
    return -1