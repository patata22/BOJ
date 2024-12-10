import heapq

dx=(-1,1,0,0)
dy=(0,0,-1,1)

n,m=map(int,input().split())
board=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='S':
            temp[j]='.'
            sx,sy=i,j
        elif temp[j]=='F':
            temp[j]='.'
            ex,ey=i,j
    board.append(temp)

for i in range(n):
    for j in range(m):
        if board[i][j]=='g':
            for d in range(4):
                nx,ny=i+dx[d],j+dy[d]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
                    board[nx][ny]='h'

board[sx][sy]='.'
board[ex][ey]='.'


q=[(0,0,sx,sy)]
distance=[[[float('inf')]*2501 for i in range(50)] for i in range(50)]
distance[sx][sy][0]=0

while q:
    garbage,near,x,y=heapq.heappop(q)
    if distance[x][y][garbage]!=near: continue
    if x==ex and y==ey:
        print(garbage, near)
        break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]=='.' and distance[nx][ny][garbage]>near:
                distance[nx][ny][garbage]=near
                heapq.heappush(q,(garbage,near,nx,ny))
            elif board[nx][ny]=='g' and distance[nx][ny][garbage+1]>near:
                distance[nx][ny][garbage+1]=near
                heapq.heappush(q,(garbage+1,near,nx,ny))
            elif board[nx][ny]=='h' and distance[nx][ny][garbage]>near+1:
                distance[nx][ny][garbage]=near+1
                heapq.heappush(q,(garbage,near+1,nx,ny))

                
