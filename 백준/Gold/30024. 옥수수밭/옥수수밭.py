import sys,heapq
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]
used=[[0]*m for i in range(n)]
q=[]
for i in range(m):
    heapq.heappush(q,(-board[0][i],0,i))
    visited[0][i]=1
    heapq.heappush(q,(-board[-1][i],n-1,i))
    visited[-1][i]=1
for i in range(1,n-1):
    heapq.heappush(q,(-board[i][0],i,0))
    visited[i][0]=1
    heapq.heappush(q,(-board[i][-1],i,m-1))
    visited[i][-1]=1

for _ in range(int(input())):
    while used[q[0][1]][q[0][2]]:
        heapq.heappop(q)
    value,x,y=heapq.heappop(q)
    print(x+1,y+1)
    used[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=1
            heapq.heappush(q,(-board[nx][ny],nx,ny))

