import heapq

dx=(-1,0,1,0)
dy=(0,-1,0,1)

def sol():
    q=[]
    sx,sy=point[0]
    ex,ey=point[1]
    for i in range(4):
        nx,ny=sx+dx[i], sy+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]!='*':
            distance[nx][ny][i]=0
            heapq.heappush(q,(0,nx,ny,i))

    while q:
        dist,x,y,d = heapq.heappop(q)
        if distance[x][y][d]!=dist: continue
        if x==ex and y==ey: return dist

        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]!='*' and distance[nx][ny][d]>dist:
            distance[nx][ny][d]=dist
            heapq.heappush(q,(dist,nx,ny,d))

        for i in (-1,1):
            D=(d+i)%4
            nx,ny=x+dx[D],y+dy[D]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]!='*' and distance[nx][ny][D]>dist+1:
                distance[nx][ny][D]=dist+1
                heapq.heappush(q,(dist+1,nx,ny,D))
                
    
            


m,n=map(int,input().split())

distance=[[[float('inf')]*4 for i in range(m)] for i in range(n)]

board=[]
point=[]
for i in range(n):
    x=tuple(input())
    for j in range(m):
        if x[j]=='C': point.append((i,j))
    board.append(x)

print(sol())
