import sys,heapq
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    n,m=map(int,input().split())
    sx,sy,ex,ey=map(lambda x: int(x)-1,input().split())
    board=[list(map(int,input().split())) for i in range(n)]
    distance=[[[float('inf')]*3 for i in range(m)] for i in range(n)]
    q=[]
    q.append((0,0,sx,sy))
    distance[sx][sy][0]=0
    
    while q:
        damage, turn, x, y = heapq.heappop(q)
        if distance[x][y][turn]!=damage: continue
        if x==ex and y==ey: return damage
        nt=(turn+1)%3
        if turn==0:
            for i in range(2):
                nx,ny=x+dx[i],y+dy[i]                
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1 and distance[nx][ny][nt]>damage+board[nx][ny]:
                    distance[nx][ny][nt]=damage+board[nx][ny]
                    heapq.heappush(q,(damage+board[nx][ny],nt,nx,ny))
        elif turn==1:
            for i in range(2,4):
                nx,ny=x+dx[i],y+dy[i]                
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1 and distance[nx][ny][nt]>damage+board[nx][ny]:
                    distance[nx][ny][nt]=damage+board[nx][ny]
                    heapq.heappush(q,(damage+board[nx][ny],nt,nx,ny))
        else:
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]                
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1 and distance[nx][ny][nt]>damage+board[nx][ny]:
                    distance[nx][ny][nt]=damage+board[nx][ny]
                    heapq.heappush(q,(damage+board[nx][ny],nt,nx,ny))
    return -1
           
print(sol())