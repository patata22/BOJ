from collections import deque

def sol():
    q=deque()
    visited=[[0]*c for i in range(r)]
    for i in range(c):
        if board[0][i]:
            q.append((0,i))
            visited[0][i]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            if x==r-1: return t
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0<=nx<r and 0<=ny<c and board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return -1
            

r,c=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(r)]
direction=[tuple(map(int,input().split())) for i in range(int(input()))]

print(sol())
