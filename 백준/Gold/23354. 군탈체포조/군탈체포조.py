import heapq

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(depth,now,d):
    global answer
    if depth==N:
        temp=dist[now][0]+d
        answer=min(answer,temp)
        return
    distance=dist[now]
    for i in range(1,N+1):
        if not used[i]:
            used[i]=1
            sol(depth+1, i, d+distance[i])
            used[i]=0
    
    

def dijkstra(x,y):
    q=[]
    distance=[[float('inf')]*n for i in range(n)]
    q.append((0,x,y))
    distance[x][y]=0
    while q:
        d,x,y=heapq.heappop(q)
        if distance[x][y]!=d: continue
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and distance[nx][ny]>d+board[nx][ny]:
                distance[nx][ny]=d+board[nx][ny]
                heapq.heappush(q,(d+board[nx][ny],nx,ny))

    D=[]
    D.append(distance[sx][sy])
    for x,y in s:
        D.append(distance[x][y])
    return D

    
n=int(input())

board=[list(map(int,input().split())) for i in range(n)]
s=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==0:  s.append((i,j))
        elif board[i][j]==-1:
            sx,sy=i,j
            board[i][j]=0
N=len(s)
dist=[]
dist.append(dijkstra(sx,sy))
for i in range(N):
    dist.append(dijkstra(*s[i]))

answer=float('inf')
used=[0]*(N+1)
sol(0,0,0)
print(answer)
