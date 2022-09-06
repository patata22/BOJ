from collections import deque
# 행=y 열=x
def bfs(v):
    q=deque()
    q.append(v)
    visited[v[0]][v[1]]=1
    while q:
        v=q.popleft()
        y=v[0]
        x=v[1]
        if x!=0:
            if farm[y][x-1]==1 and visited[y][x-1]==0:
                visited[y][x-1]=1
                q.append([y,x-1])
        if y!=0:
            if farm[y-1][x]==1 and visited[y-1][x]==0:
                visited[y-1][x]=1
                q.append([y-1,x])
        if x!=m-1:
            if farm[y][x+1]==1 and visited[y][x+1]==0:
                visited[y][x+1]=1
                q.append([y,x+1])
        if y!=n-1:
            if farm[y+1][x]==1 and visited[y+1][x]==0:
                visited[y+1][x]=1
                q.append([y+1,x])
                  
t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    farm=[[0]*m for i in range(n)]
    visited=[[0]*m for i in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        farm[y][x]=1
    answer=0
    for y in range(n):
        for x in range(m):
            if farm[y][x]==1 and visited[y][x]==0:
                answer+=1
                bfs([y,x])
    print(answer)
    
