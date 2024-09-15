from collections import deque
import sys
input=sys.stdin.readline

def makeTree():
    q=deque()
    q.append(1)
    visited[1]=1
    depth[1]=0
    dep=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    parent[to]=now
                    depth[to]=dep
                    q.append(to)
        dep+=1
    
def sol(a,b):
    if depth[a]<depth[b]:
        a,b=b,a
    while depth[a]>depth[b]:
        a=parent[a]
    if a==b: return b
    while parent[a]!=parent[b]:
        a=parent[a]
        b=parent[b]
    return parent[a]

n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
parent=[-1]*(n+1)
depth=[-1]*(n+1)

makeTree()

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(sol(a,b))
