from collections import deque
import sys
input=sys.stdin.readline

def travel(x):
    q=deque()
    q.append(x)
    distance=[-1]*(n+1)
    distance[x]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if distance[to]==-1:
                    distance[to]=t
                    q.append(to)
        t+=1
    return distance
            

n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

a,b,c=map(int,input().split())
answer='NO'
distanceA=travel(a)
distanceB=travel(b)
distanceC=travel(c)
for i in range(1,n+1):
    if len(graph[i])!=1: continue
    if distanceA[i]<distanceB[i] and distanceA[i]<distanceC[i]:
        answer='YES'
        break

print(answer)
