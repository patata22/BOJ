from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    q.append(0)
    visited=[0]*(n+1)
    visited[0]=1
    result=0
    for x in travel: visited[x]=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append(to)
                result+=1
    return result
    
n,m,k=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)

travel=set(map(lambda x:int(x)-1,input().split()))

print(sol())
