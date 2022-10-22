import sys
from collections import deque
input=sys.stdin.readline

def sol():
    q=deque()
    q.append((r,c,0))
    visited[r][c][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,now=q.popleft()
            if now==6: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny][now] and board[nx][ny]>=0:
                    visited[nx][ny][now]=1
                    if board[nx][ny]==now+1:
                        q.append((nx,ny,now+1))
                    else: q.append((nx,ny,now))
        t+=1
    return -1
    


dx=(-1,1,0,0)
dy=(0,0,-1,1)

board=[tuple(map(int,input().split())) for i in range(5)]
visited=[[[0]*7 for i in range(5)] for i in range(5)]

r,c=map(int,input().split())

print(sol())
