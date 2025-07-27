import sys,heapq
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    q=[]
    q.append((0,x,y))
    distance=[[float('inf')]*1010 for i in range(1010)]
    distance[x][y]=0

    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]!=dist:continue
        if not x and not y: return dist
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if -3<=nx<1010 and -3<=ny<1010 and distance[nx][ny]>dist+board[nx][ny]:
                distance[nx][ny]=dist+board[nx][ny]
                heapq.heappush(q,(dist+board[nx][ny],nx,ny))

n,x,y=map(int,input().split())

board=[[0]*1010 for i in range(1010)]

for _ in range(n):
    a,b=map(int,input().split())
    board[a][b]=1

print(sol(x,y))
