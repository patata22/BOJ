import sys,heapq
input=sys.stdin.readline

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)
dz=(1,1,0,1,0,1,1,0)


def sol():
    q=[]
    q.append((0,sx,sy))
    distance=[[float('inf')]*m for i in range(n)]
    distance[sx][sy]=0
    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]!=dist: continue
        if x==ex and y==ey: return dist
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
                if distance[nx][ny]>dist+dz[i]:
                    distance[nx][ny]=dist+dz[i]
                    heapq.heappush(q,(dist+dz[i],nx,ny))

    return -1
            
n,m=map(int,input().split())
board=[list(input().rstrip()) for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]=='K':
            sx,sy=i,j
            board[i][j]='.'
        elif board[i][j]=='*':
            ex,ey=i,j
            board[i][j]='.'

print(sol())