import sys,heapq
input=sys.stdin.readline

def dijkstra():
    q=[]
    q.append((0,2))
    distance[2]=0
    while q:
        d,now=heapq.heappop(q)
        if distance[now]!=d:continue
        for to,dist in graph[now]:
            if distance[to]>d+dist:
                distance[to]=d+dist
                heapq.heappush(q,(d+dist, to))

def sol():
    q=[]
    q.append((-distance[1],1,1))
    answer[1]=1
    while q:
        d,count,now=heapq.heappop(q)
        if answer[now]!=count:continue
        for to,dist in graph[now]:
            if distance[to]<-d:
                answer[to]+=answer[now]
                heapq.heappush(q,(-distance[to],answer[to],to))
    

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance=[float('inf')]*(n+1)
dijkstra()
answer=[0]*(n+1)
sol()
print(answer[2])
