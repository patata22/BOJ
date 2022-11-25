from collections import deque
import sys,heapq
input=sys.stdin.readline

def dijkstra():
    q=[]
    q.append((0,s))
    distance[s]= 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to, d in graph[now]:
            if not short[now][to] and distance[to]>dist+d:
                distance[to] = dist+d
                heapq.heappush(q,(dist+d, to))

def bfs():
    q=deque()
    q.append(e)
    temp=[0]*n
    while q:
        now = q.popleft()
        if temp[now]:continue
        temp[now]=1
        for to,d in graph_reverse[now]:
            if distance[now]==distance[to]+d:
                short[to][now]=1
                q.append(to)

while True:
    n,m = map(int,input().split())
    if not n: break
    s,e = map(int,input().split())
    graph = [[] for i in range(n)]
    graph_reverse = [[] for i in range(n)]
    short = [[0]*n for i in range(n)]
    for _  in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph_reverse[b].append((a,c))
    
    distance= [float('inf')]*n
    dijkstra()
    bfs()
    distance = [float('inf')]*n
    dijkstra()
    print(-1) if distance[e]==float('inf') else print(distance[e])
    
