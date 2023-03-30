import heapq

dx=(-1,0,1,0)
dy=(0,-1,0,1)

def solution(board):
    n=len(board)
    distance=[[[float('inf')]*2 for i in range(n)] for i in range(n)]
    
    q=[]
    for i in range(2):
        q.append((0,0,0,i))
        distance[0][0][i]=0
    
    while q:
        cost, x, y, direction = heapq.heappop(q)
        if distance[x][y][direction]!=cost:continue
        if x==n-1 and y==n-1: return cost
        
        if direction==0:
            for d in (0,2):
                nx, ny= x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                    if distance[nx][ny][0]>cost+100:
                        distance[nx][ny][0]=cost+100
                        heapq.heappush(q,(cost+100,nx,ny,0))
            for d in (1,3):
                nx, ny= x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                    if distance[nx][ny][1]>cost+600:
                        distance[nx][ny][1]=cost+600
                        heapq.heappush(q,(cost+600,nx,ny,1))
        else:
            for d in (1,3):
                nx, ny= x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                    if distance[nx][ny][1]>cost+100:
                        distance[nx][ny][1]=cost+100
                        heapq.heappush(q,(cost+100,nx,ny,1))
            for d in (0,2):
                nx, ny= x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                    if distance[nx][ny][0]>cost+600:
                        distance[nx][ny][0]=cost+600
                        heapq.heappush(q,(cost+600,nx,ny,0))
                
                
            
                
                        