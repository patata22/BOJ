import sys,heapq
input=sys.stdin.readline

def dijkstra(start,end):
    heap=[]
    distance=[float('inf')]*(n+1)
    heapq.heappush(heap,[0,start])
    distance[start]=0
    while heap:
        d,now=heapq.heappop(heap)
        if distance[now]==d:
            for v,w in graph[now]:
                if distance[v]>d+w:
                    distance[v]=d+w
                    heapq.heappush(heap,[d+w,v])
    return distance[end]

n,m,x=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
answer=0
for i in range(1,n+1):
    answer=max(answer,dijkstra(i,x)+dijkstra(x,i))

print(answer)
