import sys
sys.setrecursionlimit(2000)
input=sys.stdin.readline

def sol(now):
    visited[now]=1
    total=0
    isLeaf=True
    for to,c in graph[now]:
        if not visited[to]:
            isLeaf=False
            total+=min(c,sol(to))
    if isLeaf and now!=1:return float('inf')
    else: return total
            

for tt in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    visited=[0]*(n+1)
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    print(sol(1))
