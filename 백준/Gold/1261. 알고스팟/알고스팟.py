import heapq

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dijkstra():
    heap=[]
    heapq.heappush(heap,[0,0,0])
    distance[0][0]=0
    while heap:
        t,y,x=heapq.heappop(heap)
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if board[ny][nx]=='0' and distance[ny][nx]>t:
                    distance[ny][nx]=t
                    heapq.heappush(heap,[t,ny,nx])
                elif board[ny][nx]=='1' and distance[ny][nx]>t+1:
                    distance[ny][nx]=t+1
                    heapq.heappush(heap,[t+1,ny,nx])


m,n=map(int,input().split())
board=[list(input()) for i in range(n)]
distance=[[float('inf')]*m for i in range(n)]
dijkstra()
print(distance[-1][-1])
