import sys,heapq
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)


def sol():
    q=[]
    q.append((0,0,0,25))
    distance[0][0][25]=0
    while True:
        dist,x,y,speed=heapq.heappop(q)
        if distance[x][y][speed]!=dist: continue
        if x==n-1 and y==m-1: return dist/v
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                newSpeed= speed+(board[x][y]-board[nx][ny])
                newDist = dist+2**(25-speed)
                if distance[nx][ny][newSpeed]>newDist:
                    distance[nx][ny][newSpeed]=newDist
                    heapq.heappush(q,(newDist,nx,ny,newSpeed))

v,n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
distance=[[[float('inf')]*51 for i in range(m)] for i in range(n)]

print(sol())