import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def sol(now):
    visited[now]=1
    total=0
    leaf=True
    for to,c in graph[now]:
        if not visited[to]:
            leaf=False
            total+=min(c,sol(to))

    if leaf: return float('inf')
    else: return total

while True:
    try:
        n,C=map(int,input().split())
        graph=[[] for i in range(n+1)]
        visited=[0]*(n+1)
        for _ in range(n-1):
            a,b,c=map(int,input().split())
            graph[a].append((b,c))
            graph[b].append((a,c))
        print(sol(C))

    except :break
