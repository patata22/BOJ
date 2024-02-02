import sys,heapq
input=sys.stdin.readline

def sol():
    q=[(0,s)]
    distance[s]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))

n,m,s,e=map(int,input().split())

graph=[[] for i in range(n+1)]
distance=[float('inf')]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

sol()
print(distance[e])
