from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(sx,sy,ex,ey):
    global answer
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey:
                answer+=t
                return
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1 

n,m,s=map(int,input().split())
board=[]
point=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='S':
            point.append((i,j,0))
            temp[j]='.'
        elif temp[j].isdigit():
            point.append((i,j,int(temp[j])))
            temp[j]='.'
    board.append(temp)

point.sort(key=lambda x: x[2])
answer=0

for i in range(s):
    sx,sy,a=point[i]
    ex,ey,b=point[i+1]
    sol(sx,sy,ex,ey)
print(answer)
