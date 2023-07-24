import sys
input=sys.stdin.readline
sys.setrecursionlimit(200000)

MAX=17

def makeDepth(now):
    for to,c in graph[now]:
        if depth[to]==-1:
            depth[to]=depth[now]+1
            parent[to][0]=now
            maxCost[to][0]=c
            minCost[to][0]=c
            makeDepth(to)
n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def findAnswer(a,b):
    if depth[a]<depth[b]: a,b=b,a
    diff= depth[a]-depth[b]
    mincost=float('inf')
    maxcost=0
    j=0
    while diff:
        if diff%2:
            maxcost = max(maxcost, maxCost[a][j])
            mincost = min(mincost, minCost[a][j])
            a = parent[a][j]
        diff//=2
        j+=1
        
    if a!=b:
        for j in range(MAX-1, -1, -1):
            if parent[a][j]!=-1 and parent[a][j]!=parent[b][j]:
                maxcost = max(maxcost, maxCost[a][j], maxCost[b][j])
                mincost = min(mincost, minCost[a][j], minCost[b][j])
                a=parent[a][j]
                b=parent[b][j]
        maxcost=max(maxcost, maxCost[a][0], maxCost[b][0])
        mincost=min(mincost, minCost[a][0], minCost[b][0])

    return mincost, maxcost
            
depth=[-1]*(n+1)
parent=[[-1]*MAX for i in range(n+1)]
maxCost = [[0]*MAX for i in range(n+1)]
minCost= [[float('inf')]*MAX for i in range(n+1)]
depth[1]=0
makeDepth(1)

for j in range(1,MAX):
    for i in range(1,n+1):
        if parent[i][j-1]!=-1:
            parent[i][j] = parent[parent[i][j-1]][j-1]
            maxCost[i][j] = max(maxCost[i][j-1], maxCost[parent[i][j-1]][j-1])
            minCost[i][j] = min(minCost[i][j-1], minCost[parent[i][j-1]][j-1])
                              
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(*findAnswer(a,b))
