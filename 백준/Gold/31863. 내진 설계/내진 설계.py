from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    for i in range(4):
        nx,ny=sx+dx[i],sy+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]!='|':
            count[nx][ny]+=1
            q.append((nx,ny))
            nx+=dx[i]
            ny+=dy[i]
            
            if 0<=nx<n and 0<=ny<m and board[nx][ny]!='|':
                count[nx][ny]+=1
                q.append((nx,ny))
    while q:
        x,y=q.popleft()
        if board[x][y]=='*' and not destroyed[x][y]:
            destroyed[x][y]=1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!='|':
                    count[nx][ny]+=1
                    q.append((nx,ny))
        elif board[x][y]=='#' and not destroyed[x][y] and count[x][y]>1:
            destroyed[x][y]=1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!='|':
                    count[nx][ny]+=1
                    q.append((nx,ny))
                   
n,m=map(int,input().split())
board=[list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]=='@':sx,sy=i,j

count=[[0]*m for i in range(n)]
destroyed=[[0]*m for i in range(n)]
sol()
answer=[0,0]
for i in range(n):
    for j in range(m):
        if board[i][j]=='*' or board[i][j]=='#':
            if destroyed[i][j]: answer[0]+=1
            else: answer[1]+=1
print(*answer)
            
            
