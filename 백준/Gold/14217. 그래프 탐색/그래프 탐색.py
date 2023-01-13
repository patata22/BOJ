import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append(1)
    distance= [-1]*(n+1)
    distance[1]=0
    t=1
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            for to in graph[now]:
                if distance[to]==-1:
                    q.append(to)
                    distance[to]=t
        t+=1
                
    print(*distance[1:])


n,m=map(int,input().split())
graph= [set() for i in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

impo = set()
for _ in range(int(input())):
    c,a,b = map(int,input().split())
    if c==1:
        graph[a].add(b)
        graph[b].add(a)
    else:
        graph[a].remove(b)
        graph[b].remove(a)

    bfs()
        
