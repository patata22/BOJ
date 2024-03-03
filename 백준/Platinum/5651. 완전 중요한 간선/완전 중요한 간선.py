from collections import deque
import sys
input=sys.stdin.readline

START=1

def makeFlow():
    while True:
        q=deque()
        q.append(START)
        prev=[-1]*(n+1)
        while q:
            now=q.popleft()
            for to in graph[now]:
                if prev[to]==-1 and capa[now][to]-flow[now][to]>0:
                    q.append(to)
                    prev[to]=now
                    if now==END: break
        if prev[END]==-1: break
        now=END
        maxFlow=float('inf')
        while now!=START:
            maxFlow=min(maxFlow,capa[prev[now]][now]-flow[prev[now]][now])
            now=prev[now]
        now=END
        while now!=START:
            flow[prev[now]][now]+=maxFlow
            flow[now][prev[now]]-=maxFlow
            now=prev[now]
            
def check(start,end):
    q=deque()
    q.append(start)
    visited=[0]*(n+1)
    while q:
        now=q.popleft()
        if now==end:  return 0
        for to in graph[now]:
            if capa[now][to]-flow[now][to]>0 and not visited[to]:
                visited[to]=1
                q.append(to)
    return 1

for tt in range(int(input())):
    n,m=map(int,input().split())
    END=n
    graph=[[] for i in range(n+1)]
    graphs=[]
    capa=[[0]*(n+1) for i in range(n+1)]
    flow=[[0]*(n+1) for i in range(n+1)]

    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        graphs.append((a,b))
        capa[a][b]+=c

    makeFlow()
    answer=0
    for a,b in graphs:
        if capa[a][b]==flow[a][b]:
            answer+=check(a,b)
    print(answer)
