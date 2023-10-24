import heapq

dx=(1,0)
dy=(0,1)

def sol():
    q=[]
    q.append((board[0][0],0,0))
    visited[0][0]=board[0][0]
    while q:
        t,x,y=heapq.heappop(q)
        if visited[x][y]!=t: continue
        if x==n-1 and y==m-1:
            return t
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]>t+board[nx][ny]:
                visited[nx][ny]=t+board[nx][ny]
                heapq.heappush(q,(t+board[nx][ny],nx,ny))
                
    return -1

n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
h=int(input())
visited=[[h+1]*m for i in range(n)]
answer=sol()
if answer==-1: print('NO')
else:
    print('YES')
    print(answer)
    
