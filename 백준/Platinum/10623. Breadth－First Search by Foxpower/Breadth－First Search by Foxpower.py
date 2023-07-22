from collections import deque

MAX=17

def getLCA(a,b):
    if depth[b]>depth[a]: a,b=b,a
    diff = depth[a]-depth[b]
    cnt=0
    while diff:
        if diff%2: a = parent[a][cnt]
        diff//=2
        cnt+=1
    if a!=b:
        for j in range(MAX-1,-1,-1):
            if parent[a][j] and parent[a][j]!=parent[b][j]:
                a=parent[a][j]
                b=parent[b][j]
        a=parent[a][0]
    return a

def bfs():
    q=deque()
    for to in graph[1]:
        q.append(to)
        depth[to]=1
    prev=1
    answer=0
    while q:
        now=q.popleft()
        for to in graph[now]:
            q.append(to)
            depth[to]=depth[now]+1
        answer+=depth[prev]+depth[now]-2*depth[getLCA(prev,now)]
        prev=now
    return answer

n=int(input())
graph=[[] for i in range(n+1)]
depth=[0]*(n+1)
parent=[[0]*17 for i in range(n+1)]
temp=list(map(int,input().split()))
for i in range(n-1):
    parent[i+2][0]=temp[i]
    graph[temp[i]].append(i+2)

for j in range(1,MAX):
    for i in range(1,n+1):
        if parent[i][j-1]!=0:
            parent[i][j]=parent[parent[i][j-1]][j-1]

print(bfs())
