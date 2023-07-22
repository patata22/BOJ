import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    global cnt, scc_cnt
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result, dfs(to))
        elif not finished[to]: result = min(result, visited[to])

    if result==visited[now]:
        scc=[]
        scc_cnt+=1
        while True:
            t=stack.pop()
            scc.append(t)
            finished[t]=1
            if t==now: break

        scc.sort()
        scc.append(-1)
        SCC.append(scc)

    return result
            
v,e=map(int,input().split())
graph=[[] for i in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    
visited=[0]*(v+1)
finished=[0]*(v+1)
cnt=0
scc_cnt=0


SCC=[]
stack=[]

for i in range(1,v+1):
    if not visited[i]:
        dfs(i)

print(scc_cnt)
SCC.sort()
for scc in SCC: print(*scc)
