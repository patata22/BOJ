from collections import deque
import sys
input=sys.stdin.readline

def makeTree():
    q=deque()
    q.append(s)
    visited[s]=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                parent[to]=now
                visited[to]=1
                q.append(to)

def sol():
    now=e
    record=[]
    while now!=0:
        record.append(now)
        now=parent[now]
    record=record[::-1]
    record.pop()
    for i in range(1,len(record),2):
        if len(graph[record[i]])>2:
            return 'Second'
    return 'First'

n,s,e=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
parent=[0]*(n+1)

makeTree()
print(sol())