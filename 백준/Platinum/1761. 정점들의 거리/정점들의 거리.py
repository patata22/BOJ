import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
MAX=16

def makeTree(now):
    for to,c in graph[now]:
        if depth[to]==-1:
            parent[to][0]=now
            depth[to]=depth[now]+1
            distance[to]=distance[now]+c
            makeTree(to)

def findLCA(a,b):
    if depth[b]>depth[a]: a,b=b,a
    diff = depth[a]-depth[b]
    j=0
    while diff:
        if diff%2: a=parent[a][j]
        diff//=2
        j+=1

    if a!=b:
        for j in range(MAX-1, -1, -1):
            if parent[a][j]!=-1 and parent[a][j]!=parent[b][j]:
                a=parent[a][j]
                b=parent[b][j]
        a=parent[a][0]
    return a

n=int(input())
graph=[[] for i in range(n+1)]
parent=[[-1]*MAX for i in range(n+1)]
depth=[-1]*(n+1)
distance=[-1]*(n+1)

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

depth[1]=0
distance[1]=0
makeTree(1)

for j in range(1,MAX):
    for i in range(1,n+1):
        if parent[i][j-1]!=-1:
            parent[i][j]=parent[parent[i][j-1]][j-1]

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(distance[a]+distance[b]-2*distance[findLCA(a,b)])
