import sys,heapq
input=sys.stdin.readline

n,m,s=map(int,input().split())
s-=1

need=tuple(map(int,input().split()))
energy=tuple(map(int,input().split()))
graph=[[] for i in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

now=0
q=[]
visited=[0]*n
heapq.heappush(q,(0,s))
visited[s]=1

while q:
    if q[0][0]>now: break
    while q and q[0][0]<=now:
        _,to=heapq.heappop(q)
        now+=energy[to]
        for t in graph[to]:
            if not visited[t]:
                visited[t]=1
                heapq.heappush(q,(need[t],t))

print(now)