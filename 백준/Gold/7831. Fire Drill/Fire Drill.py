from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def search():
    q=deque()
    q.append((0,sx,sy))
    visited=[[[0]*m for i in range(n)] for i in range(l)]
    visited[0][sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            z,x,y=q.popleft()
            if board[z][x][y].isnumeric(): time[int(board[z][x][y])]=3*t
            elif board[z][x][y]=='U':
                if not visited[z+1][x][y]:
                    visited[z+1][x][y]=1
                    q.append((z+1,x,y))
            elif board[z][x][y]=='D':
                if not visited[z-1][x][y]:
                    visited[z-1][x][y]=1
                    q.append((z-1,x,y))
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[z][nx][ny]!='X' and not visited[z][nx][ny]:
                    visited[z][nx][ny]=1
                    q.append((z,nx,ny))
        t+=1

def calc():
    dp=[[0]*(q+1) for i in range(p+1)]
    for i in range(1,p+1):
        w,v=time[i],score[i]
        for j in range(q+1):
            if j<w: dp[i][j]=dp[i-1][j]
            else: dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
    return dp[-1][-1]
    
for tt in range(int(input())):
    l,n,m,p,q=map(int,input().split())
    board=[]
    for k in range(l):
        tempp=[]
        for i in range(n):
            temp=list(input().rstrip())
            for j in range(m):
                if temp[j]=='S': sx,sy=i,j
            tempp.append(temp)
        board.append(tempp)

    score=[0]*(p+1)
    time=[float('inf')]*(p+1)

    for i in range(1,p+1):
        z,x,y,s=map(int,input().split())
        board[z-1][x-1][y-1]=str(i)
        score[i]=s
    
    search()
    print(calc())