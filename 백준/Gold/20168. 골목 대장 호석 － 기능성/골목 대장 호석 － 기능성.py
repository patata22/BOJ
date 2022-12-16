import sys,heapq
input=sys.stdin.readline

def dijkstra():
    q=[]
    q.append((0,g,s))
    distance[s]=0
    while q:
        most, money, now = heapq.heappop(q)
        if distance[now]!=most: continue
        if now==e: return most
        for to, cost in graph[now]:
            if distance[to]>max(cost,most) and money>=cost:
                distance[to] = max(cost,most)
                heapq.heappush(q,(max(cost,most), money-cost, to))
                
    return -1


n,m,s,e,g = map(int,input().split())

graph= [[] for i in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance= [float('inf')]*(n+1)

print(dijkstra())
