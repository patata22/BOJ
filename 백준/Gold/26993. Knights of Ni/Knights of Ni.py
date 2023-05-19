from collections import deque
dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy,0))
    visited[sx][sy][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,z = q.popleft()
            if board[x][y]==3 and z: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=1 and not visited[nx][ny][z]:
                    if not z and board[nx][ny]==4:
                        visited[nx][ny][1]=1
                        q.append((nx,ny,1))
                    else:
                        visited[nx][ny][z]=1
                        q.append((nx,ny,z))
        t+=1

m,n=map(int,input().split())

board=[[0]*m for i in range(n)]
number=[]
while True:
    try:
        number+=list(map(int,input().split()))
    except:
        break
x=0
y=0
for i in range(n*m):
    board[x][y]=number[i]
    if number[i]==2: sx,sy=x,y
    y+=1
    if y%m==0:
        x+=1
        y=0
visited=[[[0]*2 for i in range(m)] for i in range(n)]        
print(sol())
