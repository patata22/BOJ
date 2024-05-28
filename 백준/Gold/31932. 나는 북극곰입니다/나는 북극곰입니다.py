import sys,heapq
input=sys.stdin.readline

def sol():
    l=-1
    r=10**9+1
    while l+1<r:
        mid=(l+r)//2
        if dijkstra(mid): l=mid
        else:r=mid
    return l

def dijkstra(wait):
    
    q=[]
    q.append((0,1))
    distance=[float('inf')]*(n+1)
    distance[1]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        if now==n: return True
        for to,d,t in graph[now]:
            if wait+dist+d<=t and distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
    
    return False

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,d,t=map(int,input().split())
    graph[a].append((b,d,t))
    graph[b].append((a,d,t))

print(sol())