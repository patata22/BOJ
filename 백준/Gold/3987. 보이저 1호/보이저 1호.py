import sys
sys.setrecursionlimit (10**6)

dx=(-1,0,1,0)
dy=(0,1,0,-1)

def sol(x,y,D,d,t):
    global answer, direction,endless
    if endless: return
    nx,ny=x+dx[d],y+dy[d]
    if 0<=nx<n and 0<=ny<m:
        if board[nx][ny]=='C':
            if t>answer:
                answer=t
                direction=D
                return
        elif board[nx][ny]=='.':
            if visited[nx][ny][d]:
                direction=D
                endless=True
                return
            else:
                visited[nx][ny][d]=1
                sol(nx,ny,D,d,t+1)
                visited[nx][ny][d]=0
        elif board[nx][ny]=='/':
            if d%2==0: nd=(d+1)%4
            else: nd=(d-1)%4
            if visited[nx][ny][nd]:
                direction=D
                endless=True
                return
            else:
                visited[nx][ny][nd]=1
                sol(nx,ny,D,nd,t+1)
                visited[nx][ny][nd]=0
        else:
            if d%2==0: nd=(d-1)%4
            else: nd=(d+1)%4
            if visited[nx][ny][nd]:
                direction=D
                endless=True
                return
            else:
                visited[nx][ny][nd]=1
                sol(nx,ny,D,nd,t+1)
                visited[nx][ny][nd]=0
                
    else: 
        if t>answer:
            answer=t
            direction=D
            return
            

n,m=map(int,input().split())
endless=False
direction=''
answer=0

board=[list(input()) for i in range(n)]
visited=[[[0]*4 for i in range(m)] for i in range(n)]
sx,sy=map(int,input().split())
sx-=1
sy-=1

temp='URDL'
for i in range(4):
    visited[sx][sy][i]=1
    sol(sx,sy,temp[i],i,0)
    visited[sx][sy][i]=0
if endless:
    print(direction)
    print('Voyager')
else:
    print(direction)
    print(answer+1)
