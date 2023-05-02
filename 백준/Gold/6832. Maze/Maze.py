from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)
d={'+':(0,4), '-':(2,4), '|':(0,2)}

def sol():
    q=deque()
    q.append((0,0))
    t=1
    visited[0][0]=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==n-1 and y==m-1: return t
            s,e=d[board[x][y]]
            for i in range(s,e):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!='*' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1


for T in range(int(input())):
    n,m=int(input()),int(input())
    board=[list(input()) for i in range(n)]
    visited=[[0]*m for i in range(n)]
    print(sol())
    