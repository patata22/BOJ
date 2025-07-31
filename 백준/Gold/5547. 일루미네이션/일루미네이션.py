from collections import deque

dx=(-1,-1,0,0,1,1)
dy=((-1,0,-1,1,-1,0),(0,1,-1,1,0,1))

def init():
    q=deque()
    q.append((0,0))
    visited=[[0]*m for i in range(n)]
    visited[0][0]=1
    out[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(6):
            nx,ny=x+dx[i],y+dy[x%2][i]
            if 0<=nx<n and 0<=ny<m and not board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                out[nx][ny]=1
                q.append((nx,ny))

m,n=map(int,input().split())
m+=2
board=[]
board.append([0]*(m))
for _ in range(n):
    board.append([0]+list(map(int,input().split()))+[0])
board.append([0]*(m))
n+=2

out=[[0]*m for i in range(n)]
init()

answer=0
for x in range(n):
    for y in range(m):
        if board[x][y]:
            for i in range(6):
                nx,ny=x+dx[i],y+dy[x%2][i]
                if 0<=nx<n and 0<=ny<m and not board[nx][ny] and out[nx][ny]:
                    answer+=1

print(answer)
           