import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    q.append((0,0,1))
    distance=[[float('inf')]*(k+1) for i in range(n+1)]
    distance[1][0]=0
    while q:
        dist,cost,now=heapq.heappop(q)
        if distance[now][cost]!=dist:continue
        if now==n: return dist
        for to,d,c in graph[now]:
            if cost+c<=k and distance[to][cost+c]>dist+d:
                distance[to][cost+c]=dist+d
                heapq.heappush(q,(dist+d,cost+c,to))
                

    return -1

k,n,r=int(input()),int(input()),int(input())
graph=[[] for i in range(n+1)]
for _ in range(r):
    a,b,d,t=map(int,input().split())
    graph[a].append((b,d,t))

print(sol())
