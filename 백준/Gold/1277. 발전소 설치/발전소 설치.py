import sys,heapq
input=sys.stdin.readline


def sol():
    q=[]
    q.append((0,1))
    distance[1]=0
    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now]!=dist: continue
        if now==n: return int(dist*1000)
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d, to))

n,w=map(int,input().split())
m=float(input())

distance=[float('inf')]*(n+1)
graph=[[] for i in range(n+1)]
point=[0]+[tuple(map(int,input().split())) for i in range(n)]
for _ in range(w):
    a,b=map(int,input().split())
    graph[a].append((b,0))
    graph[b].append((a,0))

for a in range(1,n+1):
    ax,ay=point[a]
    for b in range(a+1,n+1):        
        bx,by=point[b]
        temp = ((ax-bx)**2+(ay-by)**2)**0.5
        
        if temp<=m:
            graph[a].append((b,temp))
            graph[b].append((a,temp))
print(sol())
