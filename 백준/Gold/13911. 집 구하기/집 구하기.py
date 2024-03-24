import sys,heapq
input=sys.stdin.readline

def dijkstra(arr,limit):
    q=[]
    distance=[float('inf')]*(n+1)
    for x in arr:
        q.append((0,x))
        distance[x]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]!=dist:continue
        for to,d in graph[now]:
            if dist+d<=limit and distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
    return distance

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

m,X=map(int,input().split())
mc=tuple(map(int,input().split()))
s,Y=map(int,input().split())
st=tuple(map(int,input().split()))

mcDistance=dijkstra(mc,X)
stDistance=dijkstra(st,Y)

answer=float('inf')
for i in range(1,n+1):
    if not mcDistance[i] or not stDistance[i]:
        continue
    answer=min(answer,mcDistance[i]+stDistance[i])

if answer==float('inf'):print(-1)
else:print(answer)
    
