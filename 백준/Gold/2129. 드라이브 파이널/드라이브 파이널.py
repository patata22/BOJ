from collections import deque

import sys
input=sys.stdin.readline

def visitable():
    q=deque()
    visited= [0]*n
    for x in cycles:
        q.append(x)
        visited[x] = 1
    while q:
        now = q.popleft()
        if now == t: return True
        for to,tire, dist in graph[now]:
            if tire>limit[now]: break
            if not visited[to]:
                visited[to] = 1
                q.append(to)
    return False

n,m,s,t = map(int,input().split())

graph = [[] for i in range(n)]
tired = [float('inf')]*n
distance= [float('inf')]*n
limit=[float('inf')]*n
tired[s]=0
distance[s]=0
for _ in range(m):
    u,v,a,c,b = map(int,input().split())
    graph[u].append((v,a,c))
    limit[u] = min(limit[u], a)
    graph[v].append((u,b,c))
    limit[v] = min(limit[v], b)
for i in range(n):
    graph[i].sort(key = lambda x: x[1])
cycle = False
cycles = []
for i in range(n):
    for now in range(n):
        if tired[now]==float('inf') or distance[now]==float('inf'): continue
        for to, tire, dist in graph[now]:
            if tire>limit[now]: break
            if tired[to]> tired[now]+tire:
                tired[to] = tired[now]+tire
                distance[to] = distance[now]+ dist
                if i== n-1:
                    cycle = True
                    cycles.append(to)
            elif tired[to] == tired[now]+tire:
                distance[to] = min(distance[to], distance[now]+dist)

    
if distance[t] == float('inf'): print("VOID")
else:
    if cycle and visitable(): print("UNBOUND")
    else: print(tired[t], distance[t])

#print(tired[t], distance[t])
