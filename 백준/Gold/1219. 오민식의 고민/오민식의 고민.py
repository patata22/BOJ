from collections import deque
import sys
input=sys.stdin.readline

def bfs():
    q=deque()
    for x in cycles:
        q.append(x)
        visited[x] = 1
    while q:
        now = q.popleft()
        for b,c in graph[now]:
            if not visited[b]:
                visited[b] = 1
                q.append(b)
        
n,s,e,m = map(int,input().split())
distance= [float('inf')]*n
graph = [[] for i in range(n)]
visited= [0]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
money = tuple(map(int,input().split()))
distance[s] = -money[s]

cycle = False
cycles= []
for i in range(n):
    for j in range(n):
        if distance[j]==float('inf'): continue
        for to,d in graph[j]:
            if distance[to]> distance[j]+d-money[to]:
                distance[to] = distance[j]+d-money[to]
                if i==n-1:
                    cycle= True
                    cycles.append(to)

if distance[e] ==float('inf'): print('gg')
else:
    if cycle: bfs()
    if cycle and visited[e]: print('Gee')
    else: print(-distance[e])
    
