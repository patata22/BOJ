from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]=='G': return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!='X' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return 0

for T in range(int(input())):
    n,m=map(int,input().split())
    board=[list(input()) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]=='S': sx,sy=i,j
    answer=sol()
    if answer: print(f'Shortest Path: {answer}')
    else: print('No Exit')