from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(now):
    global cnt, scc_cnt
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result,dfs(to))
        elif not finished[to]: result=min(result,visited[to])

    if result==visited[now]:
        scc=[]
        while True:
            t=stack.pop()
            scc_num[t]=scc_cnt
            scc.append(t)
            finished[t]=1
            if t==now: break
        scc_cnt+=1
        SCC.append(scc)
    return result

def makeIndegree():
    q=deque()
    indegree=[0]*scc_cnt
    visited=[0]*scc_cnt
    q.append(scc_num[s])
    while q:
        now=SCC[q.popleft()]
        for node in now:
            for to in graph[node]:
                if scc_num[node]!=scc_num[to]:
                    indegree[scc_num[to]]+=1
                    if not visited[scc_num[to]]:
                        visited[scc_num[to]]=1
                        q.append(scc_num[to])
    return indegree

def sol():
    q=deque()
    q.append(scc_num[s])
    city=[0]*scc_cnt
    while q:
        scc_num_now = q.popleft()
        now = SCC[scc_num_now]
        city[scc_num_now]+=len(now)
        if scc_num_now==scc_num[t]:return city[scc_num_now]
        for node in now:
            for to in graph[node]:
                if scc_num[node]!=scc_num[to]:
                    city[scc_num[to]]=max(city[scc_num[to]],city[scc_num_now])
                    indegree[scc_num[to]]-=1
                    if indegree[scc_num[to]]==0:
                        q.append(scc_num[to])
    return 0

n,m,s,t=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
visited=[0]*(n+1)
finished=[0]*(n+1)
scc_num=[0]*(n+1)
SCC=[]
scc_cnt=0
cnt=0
stack=[]

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

indegree = makeIndegree()
print(sol())
