import sys,heapq
input=sys.stdin.readline

def sol():
    while start:
        cost,origin,now=heapq.heappop(start)
        if distance[origin][now]!=cost:continue
        if origin==now: return cost
        for to,c in graph[now]:
            if distance[origin][to]>cost+c:
                distance[origin][to]=cost+c
                heapq.heappush(start,(cost+c, origin,to))
    return -1



n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[[float('inf')]*(n+1) for i in range(n+1)]
start=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    distance[a][b]=c
    heapq.heappush(start, (c,a,b))

print(sol())
