import sys
input=sys.stdin.readline

def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if house[to]==0 or (not visited[house[to]] and dfs(house[to])):
            cow[x]=to
            house[to]=now
            return 1
    return 0
            

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]

for i in range(1,n+1):
    for x in list(map(int,input().split()))[1:]:
        graph[i].append(x)
cow=[0]*(m+1)
house=[0]*(m+1)
answer=0

for i in range(1,n+1):
    visited=[0]*(n+1)
    answer+=dfs(i)
print(answer)