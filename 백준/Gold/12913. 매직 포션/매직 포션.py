import heapq

def sol():
    q=[]
    q.append((0,0,0))
    distance[0][0]=0
    while q:
        dist,now,jump=heapq.heappop(q)
        if distance[now][jump]!=dist:continue
        if now==1: return dist/2
        for d,to in graph[now]:
            if distance[to][jump]>dist+2*d:
                distance[to][jump]=dist+2*d
                heapq.heappush(q,(dist+2*d,to,jump))
            if jump+1<=k and distance[to][jump+1]>dist+d:
                distance[to][jump+1]=dist+d
                heapq.heappush(q,(dist+d,to,jump+1))
            

n,k=map(int,input().split())

graph=[[] for i in range(n)]
for i in range(n):
    temp=list(map(int,input()))
    for j in range(i+1,n):
        graph[i].append((temp[j],j))
        graph[j].append((temp[j],i))
distance=[[float('inf')]*(k+1) for i in range(n)]
print(sol())
