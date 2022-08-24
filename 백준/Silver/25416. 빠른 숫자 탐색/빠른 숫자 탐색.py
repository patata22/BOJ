from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((r,c))
    visited[r][c]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]==1: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and board[nx][ny]>=0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1

board=[list(map(int,input().split())) for i in range(5)]
visited=[[0]*5 for i in range(5)]
r,c=map(int,input().split())
print(sol())
