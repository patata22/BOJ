import sys,heapq
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=[]
    distance=[[float('inf')]*n for i in range(n)]
    distance[0][0]=board[0][0]
    q.append((board[0][0],0,0))
    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]!=dist: continue
        if x==n-1 and y==n-1: return dist
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and distance[nx][ny]>dist+board[nx][ny]:
                distance[nx][ny]=dist+board[nx][ny]
                heapq.heappush(q,(dist+board[nx][ny],nx,ny))
    
tt=0
while True:
    tt+=1
    n=int(input())
    if not n: break
    board=[tuple(map(int,input().split())) for i in range(n)]
    print(f'Problem {tt}: {sol()}')