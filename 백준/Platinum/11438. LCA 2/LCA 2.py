import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

MAX = 17

def makeTree(now):
    for to in graph[now]:
        if(depth[to]==-1):
            parent[to][0]=now
            depth[to]=depth[now]+1
            makeTree(to)

n=int(input())
graph= [[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
            
parent=[[-1]*MAX for i in range(n+1)]
depth=[-1]*(n+1)
depth[1]=0

makeTree(1)
for j in range(1,MAX):
    for i in range(1,n+1):
        parent[i][j]=parent[parent[i][j-1]][j-1]

for _ in range(int(input())):
    a,b=map(int,input().split())
    if depth[a]<depth[b]:
        a,b=b,a
    diff = depth[a]-depth[b]
    j=0
    while diff:
        if diff%2: a = parent[a][j]
        diff//=2
        j+=1
    if a!=b:
        for j in range(MAX-1,-1,-1):
            if parent[a][j]!=-1 and parent[a][j]!=parent[b][j]:
                a=parent[a][j]
                b=parent[b][j]
        a=parent[a][0]
    print(a)
