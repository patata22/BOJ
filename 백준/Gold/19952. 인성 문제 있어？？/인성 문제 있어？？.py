from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((xs,ys))
    visited[xs][ys]=1
    t=0
    while q and t<=f:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==xe and y==ye: return "잘했어!!"
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if board[nx][ny]>board[x][y] and f-t>=board[nx][ny]-board[x][y]:
                        visited[nx][ny]=1
                        q.append((nx,ny))
                    elif board[nx][ny]<=board[x][y]:
                        visited[nx][ny]=1
                        q.append((nx,ny))
        t+=1
    return "인성 문제있어??"


for _ in range(int(input())):
    n,m,o,f,xs,ys,xe,ye=map(int,input().split())
    board=[[0]*m for i in range(n)]
    for __ in range(o):
        x,y,l=map(int,input().split())
        board[x-1][y-1]=l
    xs-=1
    ys-=1
    xe-=1
    ye-=1
    visited=[[0]*m for i in range(n)]
    print(sol())
        
