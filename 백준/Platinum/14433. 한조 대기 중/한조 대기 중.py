import sys
input=sys.stdin.readline

def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if not troll[to] or (not visited[troll[to]] and dfs(troll[to])):
            troll[to]=now
            return 1
    return 0

n,m,k1,k2=map(int,input().split())
result=[]
for k in (k1,k2):
    graph=[[] for i in range(n+1)]
    troll=[0]*(m+1)
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a].append(b)
    answer=0
    for i in range(1,n+1):
        visited=[0]*(n+1)
        answer+=dfs(i)
    result.append(answer)

if result[0]>=result[1]:print("그만 알아보자")
else:print("네 다음 힐딱이")
