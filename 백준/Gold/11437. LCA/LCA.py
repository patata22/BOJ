import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)


def makeTree(now,dep,parent):
    p[now]=parent
    depth[now]=dep
    for to in graph[now]:
        if depth[to]==-1:
            makeTree(to,dep+1,now)

def lca(a,b):
    if depth[a]<depth[b]:
        a,b=b,a
    diff=depth[a]-depth[b]

    for i in range(diff):
        a=p[a]
    while p[a]!=p[b]:
        a=p[a]
        b=p[b]
    if a==b:return a
    return p[a]

n=int(input())
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

p=[-1]*(n+1)
depth=[-1]*(n+1)

makeTree(1,0,-1)
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(lca(a,b))
