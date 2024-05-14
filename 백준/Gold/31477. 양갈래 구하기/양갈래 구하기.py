import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(now):
    visited[now]=1
    leaf=True
    total=0
    for to,c in graph[now]:
        if not visited[to]:
            leaf=False
            total+=min(c,sol(to))
    if leaf: return float('inf')
    else: return total


n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited=[0]*(n+1)
print(sol(1))
