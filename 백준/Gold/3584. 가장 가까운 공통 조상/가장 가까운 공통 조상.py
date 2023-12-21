import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def makeTree(now):
    for to in graph[now]:
        if depth[to]==-1:
            depth[to]=depth[now]+1
            parent[to]=now
            makeTree(to)
            

for __ in range(int(input())):
    n=int(input())
    parent=[0]*(n+1)
    depth=[-1]*(n+1)
    isRoot=[1]*(n+1)
    graph=[[] for i in range(n+1)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        isRoot[b]=0
    for i in range(1,n+1):
        if isRoot[i]: r=i
    parent[r]=r
    depth[r]=0
    makeTree(r)

    a,b=map(int,input().split())
    if depth[a]<depth[b]:a,b=b,a
    while depth[a]!=depth[b]:
        a=parent[a]
    while a!=b:
        a,b=parent[a],parent[b]
    print(a)
   