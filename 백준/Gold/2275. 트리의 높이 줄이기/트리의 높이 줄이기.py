from collections import deque
import sys
input=sys.stdin.readline

def bottomUp():
    q=deque()
    for i in range(1,n+1):
        if not graph[i]:
            q.append(i)
    while q:
        now=q.popleft()
        if now==root: continue
        to,dist=parent[now]
        distance[to]=max(distance[to],distance[now]+dist)
        indegree[to]-=1
        if not indegree[to]: q.append(to)

def topDown():
    result=0
    q=deque()
    q.append((root,0))
    while q:
        now,prefix=q.popleft()
        for to,dist in graph[now]:
            cut=0
            totalDist=prefix+dist+distance[to]
            if totalDist>h:
                cut=min(totalDist-h,dist)
                result+=cut
            q.append((to,prefix+dist-cut))
    return result
        
n,h=map(int,input().split())
graph=[[] for i in range(n+1)]
indegree=[0]*(n+1)
parent=[0]*(n+1)

for i in range(1,n+1):
    a,b=map(int,input().split())
    if a==0: root=i
    graph[a].append((i,b))
    parent[i]=(a,b)
    indegree[a]+=1

distance=[0]*(n+1)
bottomUp()
print(topDown())
