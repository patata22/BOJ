from collections import deque
import sys
input=sys.stdin.readline

DIV=1000000007


def travel(x):
    q=deque()
    q.append(x)
    result=1
    visited[x]=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                result+=1
                q.append(to)
    return result

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
answer=1
for i in range(1,n+1):
    if not visited[i]:
        answer=(answer*travel(i))%DIV

print(answer)
        
