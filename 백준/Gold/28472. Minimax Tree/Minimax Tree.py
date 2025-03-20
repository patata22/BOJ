import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def sol(now,depth):
    visited[now]=1
    if isLeaf[now]: return value[now]
    isMax = 1-depth%2
    if isMax:
        result=-float('inf')
        for to in graph[now]:
            if not visited[to]:
                result=max(sol(to,depth+1),result)
    else:
        result=float('inf')
        for to in graph[now]:
            if not visited[to]:
                result=min(sol(to,depth+1),result)
    value[now]=result
    return result

n,r=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

isLeaf=[0]*(n+1)
value=[0]*(n+1)
visited=[0]*(n+1)
for _ in range(int(input())):
    k,t=map(int,input().split())
    value[k]=t
    isLeaf[k]=1

sol(r,0)

for _ in range(int(input())):
    print(value[int(input())])