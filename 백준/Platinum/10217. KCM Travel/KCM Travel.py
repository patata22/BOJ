import sys,heapq
input=sys.stdin.readline

def dijkstra():
    q=[]
    q.append((0,0,1))
    distance[1][0]=0
    while q:
        time, cost, now = heapq.heappop(q)
        if distance[now][cost]!=time: continue
        if now == n: return time
        for v,c,d in graph[now]:
            C=cost+c
            T=time+d
            if C<=m and distance[v][C]>T:
                for p in range(C,m+1):
                    if distance[v][p]>T:distance[v][p]=T
                    else: break
                heapq.heappush(q,(time+d,cost+c,v))
    return 'Poor KCM'


for _ in range(int(input())):
    n,m,k=map(int,input().split())
    distance= [[float('inf')]*(m+1) for i in range(n+1)]
    graph = [[] for i in range(n+1)]
    for _ in range(k):
        u,v,c,d=map(int,input().split())
        graph[u].append((v,c,d))
    print(dijkstra())
