from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((r,c))
    visited=[[0]*5 for i in range(5)]
    visited[r][c]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            if board[x][y] == 1: return t
            for i in range(4):
                nx,ny= x+dx[i],y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and board[nx][ny]!=-1 and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                nx,ny= x,y
                while True:
                    mx,my= nx+dx[i], ny+dy[i]
                    if not (0<=mx<5 and 0<=my<5):
                        if not visited[nx][ny]:
                            visited[nx][ny]=1
                            q.append((nx,ny))
                        break
                    else:
                        if board[mx][my]==-1:
                            if not visited[nx][ny]:
                                visited[nx][ny]=1
                                q.append((nx,ny))
                            break
                        elif board[mx][my]==7:
                            if not visited[mx][my]:
                                visited[mx][my]=1
                                q.append((mx,my))
                            break
                    nx,ny=mx,my
        t+=1
    return -1
board=[tuple(map(int,input().split())) for i in range(5)]
r,c=map(int,input().split())
print(sol())
