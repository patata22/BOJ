import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)

def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if work[to]==0 or (not visited[work[to]] and dfs(work[to])):
            worker[now]=to
            work[to]=now
            return 1
    return 0


n,m=map(int,input().split())
graph=[[] for i in range(n+1)]

for i in range(1,n+1):
    for x in list(map(int,input().split()))[1:]:
        graph[i].append(x)

worker=[0]*(n+1)
work=[0]*(m+1)
answer=0

for i in range(1,n+1):
    visited=[0]*(n+1)
    answer+=dfs(i)
print(answer)