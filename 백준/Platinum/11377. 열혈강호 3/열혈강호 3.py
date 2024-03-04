import sys
input=sys.stdin.readline


def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if not work[to] or (not visited[work[to]] and dfs(work[to])):
            work[to]=now
            worker[now]=to
            return 1
    return 0
                            
n,m,k=map(int,input().split())

graph=[[] for i in range(2*n+2)]
worker=[0]*(2*n+2)
work=[0]*(m+1)

for i in range(1,n+1):
    for x in list(map(int,input().split()))[1:]:
        graph[2*i].append(x)
        graph[2*i+1].append(x)

answer=0

for i in range(1,n+1):
    visited=[0]*(2*n+2)
    answer+=dfs(2*i)

count=0
for i in range(1,n+1):
    visited=[0]*(2*n+2)
    result = dfs(2*i+1)
    answer+=result
    count+=result
    if count==k: break
print(answer)
