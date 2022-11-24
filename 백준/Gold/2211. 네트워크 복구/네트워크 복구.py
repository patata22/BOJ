import sys,heapq
input= sys.stdin.readline

def sol():
    q=[]
    q.append((0,1))
    distance[1]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to] = dist+d
                prev[to] = now
                heapq.heappush(q, (dist+d, to))
    



n,m= map(int,input().split())

graph = [[] for i in range(n+1)]
prev = [-1]*(n+1)
distance = [float('inf')]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

sol()
print(n-1)
for i in range(2,n+1):
    print(i,prev[i])
