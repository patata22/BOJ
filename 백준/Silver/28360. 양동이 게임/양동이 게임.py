from collections import deque

def sol():
    q=deque()
    q.append(1)
    while q:
        now=q.popleft()
        if not water[now]: continue
        if len(graph[now]):
            w = water[now]/len(graph[now])
            for to in graph[now]:
                q.append(to)
                water[to]+=w
            water[now]=0
    
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

water=[0]*(n+1)
water[1]=100
sol()
print(max(water))
