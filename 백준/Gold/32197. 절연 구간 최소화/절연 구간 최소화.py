import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    q.append((0,0,s))
    q.append((0,1,s))
    distance=[[float('inf')]*2 for i in range(n+1)]
    distance[s][0]=0
    distance[s][1]=0
    while q:
        dist,typ,now = heapq.heappop(q)
        if distance[now][typ]!=dist: continue
        if now==e: return dist
        for to,ty in graph[now]:
            if ty!=typ and distance[to][ty]>dist+1:
                distance[to][ty]=dist+1
                heapq.heappush(q,(dist+1, ty,to))
            elif ty==typ and distance[to][typ]>dist:
                distance[to][typ]=dist
                heapq.heappush(q,(dist,typ,to))
    
            

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,e=map(int,input().split())

print(sol())
