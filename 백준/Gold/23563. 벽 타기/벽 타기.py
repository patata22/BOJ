import sys,heapq

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=[]
    q.append((0,sx,sy))
    distance[sx][sy]=0
    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]!=dist: continue
        if x==ex and y==ey: return dist
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
                if nearWall[x][y] and nearWall[nx][ny] and distance[nx][ny]>dist:
                    distance[nx][ny]=dist
                    heapq.heappush(q, (dist,nx,ny))
                elif board[nx][ny]=='.' and distance[nx][ny]>dist+1:
                    distance[nx][ny]=dist+1
                    heapq.heappush(q,(dist+1,nx,ny))
            
                    
n,m=map(int,input().split())
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='S':
            sx,sy=i,j
            x[j]='.'
        elif x[j]=='E':
            ex,ey=i,j
            x[j]='.'
    board.append(x)
distance=[[float('inf')]*m for i in range(n)]
nearWall = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]=='#':
            for k in range(4):
                nx,ny=i+dx[k],j+dy[k]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
                    nearWall[nx][ny]=1

print(sol())
    