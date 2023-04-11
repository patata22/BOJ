import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    q.append((0,1,1000))
    distance[1][1000]=0
    while q:
        cost, now, minFlow=heapq.heappop(q)
        if distance[now][minFlow]!=cost:continue
        for to, c, f in graph[now]:
            temp=min(minFlow,f)
            if distance[to][temp]>cost+c:
                distance[to][temp]=cost+c
                heapq.heappush(q,(cost+c, to, temp))

n,m=map(int,input().split())
distance=[[float('inf')]*1001 for i in range(n+1)]

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c,d=map(int,input().split())
    graph[a].append((b,c,d))
    graph[b].append((a,c,d))

sol()
answer=0
for i in range(1,1001):
    if distance[-1][i]==float('inf'): continue
    answer=max(answer,1000000*i/distance[-1][i])
print(int(answer))
