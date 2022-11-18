from collections import deque

dx = (1,0)
dy = (0,1)

def sol():
    q=deque()
    q.append((0,0))
    while q:
        x,y= q.popleft()
        z= board[x][y]
        if z==-1: return 'HaruHaru'
        elif z==0: continue
        for i in range(2):
            nx,ny= x+z*dx[i], y+z*dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

    return 'Hing'
           
n=int(input())

board = [tuple(map(int,input().split())) for i in range(n)]
visited= [[0]*n for i in range(n)]
print(sol())
