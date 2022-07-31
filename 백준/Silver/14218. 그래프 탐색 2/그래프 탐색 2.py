#14218

from collections import deque
import sys
input=sys.stdin.readline

def start():
    q=deque()
    q.append(1)
    distance[1]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for x in graph[now]:
                if distance[x]==-1 or distance[x]>t:
                    distance[x]=t
                    q.append(x)
        t+=1

def connect(n):
    q=deque()
    q.append(n)
    t=distance[n]+1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for x in graph[now]:
                if distance[x]==-1 or distance[x]>t:
                    distance[x]=t
                    q.append(x)
        t+=1

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
distance = [-1]*(n+1)

for _ in range(m):
    a,b,=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

start()

for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    if distance[a]!=-1:
        if distance[b]==-1 or distance[b]>distance[a]+1:
            distance[b]=distance[a]+1
            connect(b)
    if distance[b]!=-1:
        if distance[a]==-1 or distance[a]>distance[b]+1:
            distance[a]=distance[b]+1
            connect(a)
    print(*distance[1:])
