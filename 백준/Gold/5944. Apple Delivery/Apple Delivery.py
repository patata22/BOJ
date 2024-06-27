import sys,heapq
input=sys.stdin.readline

def sol(x):
    q=[]
    distance=[float('inf')]*(n+1)
    q.append((0,x))
    distance[x]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist:continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))

    return distance

m,n,start,end1,end2=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance1=sol(start)
distance2=sol(end1)
print(min(distance1[end1],distance1[end2])+distance2[end2])
