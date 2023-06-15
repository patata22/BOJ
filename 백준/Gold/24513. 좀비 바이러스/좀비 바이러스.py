from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((fx,fy,1))
    q.append((sx,sy,2))
    
    visited[fx][fy][0]=1
    visited[sx][sy][1]=1
    t=2
    while q:
        for _ in range(len(q)):
            x,y,vtype = q.popleft()
        
            if visited[x][y][0]==visited[x][y][1]:
                answer[2]+=1
                continue
            else: answer[vtype-1]+=1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1 and not visited[nx][ny][vtype-1] and (not visited[nx][ny][2-vtype] or visited[nx][ny][2-vtype]==t):
                    visited[nx][ny][vtype-1]=t
                    q.append((nx,ny,vtype))
                
        t+=1
        
n,m=map(int,input().split())

board=[]
for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(m):
        if temp[j]==1:
            fx,fy=i,j
            temp[j]=0
        elif temp[j]==2:
            sx,sy=i,j
            temp[j]=0
    board.append(temp)

visited=[[[0]*2 for i in range(m)] for i in range(n)]


answer=[0,0,0]
sol()
answer[2]//=2
print(*answer)