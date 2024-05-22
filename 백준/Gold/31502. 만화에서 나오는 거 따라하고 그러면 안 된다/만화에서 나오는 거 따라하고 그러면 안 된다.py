import sys,heapq
input=sys.stdin.readline
from collections import deque

def han():
    q=deque()
    q.append(B)
    visited=[0]*(n+1)
    prev=[-1]*(n+1)
    visited[B]=1
    while q:
        now=q.popleft()
        for to,c in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append(to)
                prev[to]=now
    now=C
    cand=[]
    while now!=-1:
        cand.append(now)
        now=prev[now]
    return sorted(cand)

def tok():
    q=[]
    q.append((0,A))
    distance=[float('inf')]*(n+1)
    distance[A]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        for to, d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
    return distance

n,m=map(int,input().split())
A,B,C=map(int,input().split())
graph=[[] for i in range(n+1)]
count=[0]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    count[a]+=1
    count[b]+=1

for i in range(n+1):
    graph[i].sort(key=lambda x: (count[x[0]],x[0]), reverse=True)

cand=han()
distance=tok()
answer=0
dist=float('inf')
for x in han():
    if distance[x]<dist:
        dist=distance[x]
        answer=x
print(answer)
