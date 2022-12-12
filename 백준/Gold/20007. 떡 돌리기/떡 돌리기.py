import sys,heapq
input=sys.stdin.readline

def dijkstra():
    q=[(0,y)]
    distance[y]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to, d in graph[now]:
            if distance[to]>dist+d:
                distance[to]= dist+d
                heapq.heappush(q, (dist+d, to))

n,m,x,y = map(int,input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance= [float('inf')]*n
dijkstra()
if max(distance)*2>x: print(-1)
else:
    distance.sort()
    day = 1
    count=0
    for d in distance:
        if count+2*d>x:
            count=2*d
            day+=1
        else:
            count+=2*d
    print(day)
    
