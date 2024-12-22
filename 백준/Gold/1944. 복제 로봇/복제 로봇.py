from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def bfs(x,y):
    start=board[x][y]
    q=deque()
    q.append((x,y))
    visited=[[0]*n for i in range(n)]
    visited[x][y]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]>0 and board[x][y]!=start: graph.append((start,board[x][y],t))
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<nx<n and 0<ny<n and board[nx][ny]>=0 and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        p[b]=a

def kruskal():
    cnt=0
    answer=0
    for a,b,c in graph:
        a,b=find(a),find(b)
        if a!=b:
            union(a,b)
            cnt+=1
            answer+=c
            if cnt==m: return answer
    return -1
    
n,m=map(int,input().split())
keyNum=2
board=[]
for i in range(n):
    temp=list(input())
    for j in range(n):
        if temp[j]=='S': temp[j]=1
        elif temp[j]=='K':
            temp[j]=keyNum
            keyNum+=1
        else:
            temp[j]=-int(temp[j])
    board.append(temp)

graph=[]
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            bfs(i,j)

graph.sort(key=lambda x: x[2])
p=[-1]*keyNum

print(kruskal())