import heapq

def sol():
    q=[]
    q.append((0,0,0)) #t, d, now
    distance=[float('inf')]*n
    distance[0]=0
    while q:
        t,d,now=heapq.heappop(q)
        if now==1: return d
        for to,dist in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(t+1,dist+d, to))
    

n,m=map(int,input().split())

graph=[[] for i in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
print(sol())
