import heapq

def sol():
    q=[]
    q.append((0,k,1<<k))
    distance[k][1<<k]=0
    while q:
        dist,now,visited = heapq.heappop(q)
        if visited== (1<<(n))-1:return dist
        if distance[now][visited]!=dist: continue
        for to in range(n):
            d=graph[now][to]
            nv = visited|(1<<to)
            if distance[to][nv]>dist+d:
                distance[to][nv]=dist+d
                heapq.heappush(q,(dist+d,to,nv))

n,k=map(int,input().split())
graph=[tuple(map(int,input().split())) for i in range(n)]
distance=[[float('inf')]*((1<<(n+1))-1) for i in range(n)]

print(sol())
