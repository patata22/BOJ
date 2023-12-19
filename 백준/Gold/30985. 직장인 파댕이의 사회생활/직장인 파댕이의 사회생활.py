import sys,heapq
input=sys.stdin.readline

def dijkstra(p):
    q=[]
    q.append((0,p))
    distance=[float('inf')]*(n+1)
    distance[p]=0
    while q:
        dist, now= heapq.heappop(q)
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d, to))
    return distance
        


n,m,k=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

elevator=tuple(map(int,input().split()))

distance_start=dijkstra(1)
distance_end=dijkstra(n)

answer=float('inf')
for i in range(1,n+1):
    if elevator[i-1]<0: continue
    temp=distance_start[i]+elevator[i-1]*(k-1)+distance_end[i]
    answer=min(answer,temp)

if answer==float('inf'): print(-1)
else: print(answer)
