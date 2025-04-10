import sys
input=sys.stdin.readline
sys.setrecursionlimit(100009)

def travel(now):
    if visited[now]: return visited[now]
    result=0
    for to in graph[now]:
        if indegree[now]<indegree[to]:
            result=max(result,travel(to))
    visited[now]=result+1
    return visited[now]
    
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
indegree=[0]*n
visited=[0]*n

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[a]+=1
    indegree[b]+=1

for i in range(n):
    if not visited[i]:
        travel(i)

print(max(visited))