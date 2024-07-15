import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    distance=[[float('inf')]*(k+1) for i in range(n+1)]
    q.append((0,0,s))
    distance[s][0]=0
    while q:
        dist,magic,now=heapq.heappop(q)
        if distance[now][magic]!=dist: continue
        if now==e: return dist
        for to,i in graph[now]:
            d=time[magic][i]
            if distance[to][magic]>dist+d:
                distance[to][magic]=dist+d
                heapq.heappush(q,(dist+d,magic,to))
            if magic+1<=k:
                d=time[magic+1][i]
                if distance[to][magic+1]>dist+d:
                    distance[to][magic+1]=dist+d
                    heapq.heappush(q,(dist+d,magic+1,to))

n,m,s,e=map(int,input().split())

graph=[[] for i in range(n+1)]
time=[[] for i in range(101)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,i))
    graph[b].append((a,i))
    time[0].append(c)
k=int(input())
for _ in range(1,k+1):
    time[_]=tuple(map(int,input().split()))


print(sol())
