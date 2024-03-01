import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6+9)

def scc(now):
    global unused,sccCnt
    unused+=1
    visited[now]=unused
    result=unused
    stack.append(now)

    for to in graph[now]:
        if not visited[to]: result=min(result,scc(to))
        elif not finished[to]: result=min(result,visited[to])

    if result==visited[now]:
        sccCnt+=1
        while True:
            t=stack.pop()
            finished[t]=1
            sccNum[t]=sccCnt
            if now==t: break
    return result
            
def topsort():
    indegree=[0]*sccCnt
    for now in range(1,n+1):
        for to in graph[now]:
            if sccNum[now]==sccNum[to]: continue
            indegree[sccNum[to]]+=1
    answer=0
    for x in indegree:
        if not x: answer+=1
    return answer
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

visited=[0]*(n+1)
finished=[0]*(n+1)

unused=0
sccCnt=0
stack=[]
sccNum=[0]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        scc(i)

print(topsort())
