from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    visited= [[0]*m for i in range(2)]
    for i in range(2):
        if board[i][0]=='.':
            q.append((i,0))
            visited[i][0]=1
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if y==m-1: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<2 and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
                    

m=int(input())
board=[]
count=0
for _ in range(2):
    temp = list(input())
    for j in range(m):
        if temp[j]=='.':count+=1
    board.append(temp)

print(count-sol())
