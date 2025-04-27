import sys,heapq
input=sys.stdin.readline

def sol(start,end):
    q=[]
    q.append((0,start))
    distance=[float('inf')]*(n+1)
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        if now==end: return dist
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
    return -1
    
n,k=map(int,input().split())
graph=[[] for i in range(n+1)]

for _ in range(k):
    temp=list(map(int,input().split()))
    if temp[0]:
        a,b,c,d=temp
        graph[b].append((c,d))
        graph[c].append((b,d))
    else: print(sol(temp[1],temp[2]))