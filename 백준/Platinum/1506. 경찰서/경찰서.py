import sys
input=sys.stdin.readline

def dfs(now):
    global cnt
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result, dfs(to))
        elif not finished[to]: result = min(result, visited[to])

    if result==visited[now]:
        scc=[]
        while True:
            t=stack.pop()
            finished[t]=1
            scc.append(t)
            if t==now: break
        SCC.append(scc)
    return result


n=int(input())
cost=tuple(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(n):
    temp=tuple(map(int,input().rstrip()))
    for j in range(n):
        if temp[j]: graph[i].append(j)
visited=[0]*n
finished=[0]*n
SCC=[]
cnt=0
stack=[]

for i in range(n):
    if not visited[i]:
        dfs(i)

answer=0
for scc in SCC:
    temp=float('inf')
    for node in scc:
        temp = min(temp, cost[node])
    answer+=temp
print(answer)
