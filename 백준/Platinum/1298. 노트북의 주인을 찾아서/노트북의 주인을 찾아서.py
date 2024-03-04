import sys
input=sys.stdin.readline

def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if not notebook[to] or (not visited[notebook[to]] and dfs(notebook[to])):
            notebook[to]=now
            return 1
    return 0
                                

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
notebook=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

answer=0

for i in range(1,n+1):
    visited=[0]*(n+1)
    answer+=dfs(i)

print(answer)
