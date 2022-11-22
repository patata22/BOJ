from collections import deque
import sys
input=sys.stdin.readline

def reverseSearch():
    q=deque()
    q.append(n)
    visitable[n]=1
    while q:
        now = q.popleft()
        for x in graph_reverse[now]:
            if not visitable[x]:
                visitable[x]= 1
                q.append(x)

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
graph_reverse= [[] for i in range(n+1)]
distance= [float('inf')]*(n+1)
visitable= [0]*(n+1)
distance[1] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,-c))
    graph_reverse[b].append(a)

prev = [-1]*(n+1)

cycle = False
cycles = []
for i in range(n):
    for j in range(1,n+1):
        for to, d in graph[j]:
            if distance[to]>distance[j]+d:
                distance[to] = distance[j]+d
                prev[to] = j
                if i==n-1:
                    cycle  = True
                    cycles.append(to)

reverseSearch()
inf=False
if cycle:
    for x in cycles:
        if visitable[x]:
            inf= True
            break
        

if inf or distance[n]==float('inf'): print(-1)
else:
    trace = []
    now = n
    while now!=-1:
        trace.append(now)
        now = prev[now]
    print(*trace[::-1])
