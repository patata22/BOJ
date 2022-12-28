from collections import deque
import sys
input=sys.stdin.readline

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
            if board[x][y] not in (0,2): return ("TAK", t)
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=1 and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return ('NIE')
                


n,m=map(int,input().split())
board = []
for _ in range(n):
    temp = tuple(map(int,list(input().rstrip())))
    for __ in range(m):
        if temp[__]==2:sx,sy = _,__
    board.append(temp)

answer=sol()
if type(answer)==tuple:
    for x in answer:print(x)
else: print(answer)
