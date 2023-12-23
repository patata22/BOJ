import heapq

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=[]
    q.append((board[0][0],0,0))
    distance[0][0]=board[0][0]
    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]!=dist:continue
        if x==n-1 and y==m-1:return dist
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]>=0 and distance[nx][ny]>dist+board[nx][ny]:
                distance[nx][ny]=dist+board[nx][ny]
                heapq.heappush(q,(dist+board[nx][ny],nx,ny))
    return -1

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
distance=[[float('inf')]*m for i in range(n)]
if board[0][0]<0 or board[n-1][m-1]<0:
    print(-1)
else:
    print(sol())
