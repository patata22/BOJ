import heapq

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    if board[sx][sy]==-1: return -1
    q=[]
    q.append((board[sx][sy],sx,sy))
    distance=[[float('inf')]*n for i in range(n)]
    distance[sx][sy]=board[sx][sy]
    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]!=dist: continue
        if x==ex and y==ey: return dist
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=-1 and distance[nx][ny]>dist+board[nx][ny]:
                distance[nx][ny]=dist+board[nx][ny]
                heapq.heappush(q,(dist+board[nx][ny],nx,ny))
    return -1

n=int(input())
sy,sx,ey,ex=map(lambda x: int(x)-1, input().split())
board=[list(map(int,input().split())) for i in range(n)]

print(sol())