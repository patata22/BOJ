import sys,heapq
input=sys.stdin.readline

def dijkstra(start):
    q=[]
    q.append((0,start))
    distance=[float('inf')]*(n+1)
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to ,c in graph[now]:
            if distance[to]>dist+c:
                distance[to]=dist+c
                heapq.heappush(q,(dist+c, to))
    return distance

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

location = list(map(int,input().split()))

time=[]
now=0
nxt=1
time.append((location[now],0))
while nxt<10:
    distance = dijkstra(location[now])
    while nxt<10 and distance[location[nxt]]==float('inf'):
        nxt+=1
    if nxt<=9:
        time.append((location[nxt], distance[location[nxt]]+time[-1][-1]))
        now=nxt
        nxt=now+1
time.sort()

flag=False
distance = dijkstra(int(input()))
for i in range(len(time)):
    now,t = time[i]
    if distance[now]<=t:
        flag=True
        print(now)
        break
if not flag: print(-1)