import heapq,sys
input=sys.stdin.readline

def sol(s,t):
    q=[]
    distance=[float('inf')]*(n+1)
    heapq.heappush(q,(0,s))
    distance[s]=0
    while q:
        c,now = heapq.heappop(q)
        if c!=distance[now]:continue
        if now==t: return c
        for to,cost in graph[now]:
            if cost+c<distance[to]:
                distance[to]=cost+c
                heapq.heappush(q,(cost+c,to))

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t=map(int,input().split())
print(sol(s,t))