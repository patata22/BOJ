from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeSCC(now):
    global unused,sccCnt
    unused+=1
    visited[now]=unused
    result=unused
    stack.append(now)

    for to in graph[now]:
        if not visited[to]: result=min(result,makeSCC(to))
        elif not finished[to]: result=min(result, visited[to])

    if result==visited[now]:
        scc=[]
        sccCnt+=1
        while True:
            t=stack.pop()
            finished[t]=1
            sccNum[t]=sccCnt
            scc.append(t)
            if now==t: break
        SCC.append(scc)

    return result

def topSort():
    indegree=[0]*(sccCnt+1)
    for now in range(1,n+1):
        for to in graph[now]:
            if sccNum[now]==sccNum[to]:continue
            indegree[sccNum[to]]+=1

    q=deque()
    for i in range(sccCnt+1):
        if not indegree[i]:
            q.append(i)
    if len(q)>1: return (0,-1)
    start=q[0]
    while q:
        scc=SCC[q.popleft()]
        for now in scc:
            for to in graph[now]:
                if sccNum[now]==sccNum[to]:continue
                indegree[sccNum[to]]-=1
                if not indegree[sccNum[to]]:
                    q.append(sccNum[to])
        if len(q)>1: return (0,-1)

    return 1,start

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

unused=0
visited=[0]*(n+1)
finished=[0]*(n+1)
stack=[]
SCC=[]
sccCnt=-1
sccNum=[0]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        makeSCC(i)

success,num=topSort()
if not success:print(0)
else:
    print(len(SCC[num]))
    print(*sorted(SCC[num]))
