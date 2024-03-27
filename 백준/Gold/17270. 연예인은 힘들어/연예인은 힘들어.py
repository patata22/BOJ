import sys,heapq
input=sys.stdin.readline

def getDistance(x):
    q=[(0,x)]
    distance=[float('inf')]*(n+1)
    distance[x]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
    return distance
    

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
j,s=map(int,input().split())

distanceJ=getDistance(j)
distanceS=getDistance(s)
total=float('inf')
for i in range(1,n+1):
    if i==j or i==s: continue
    total=min(total,distanceJ[i]+distanceS[i])
    
answer=[]        
for i in range(1,n+1):
    if i==j or i==s: continue
    if distanceJ[i]+distanceS[i]==total:
        if distanceJ[i]<=distanceS[i]:
            answer.append(i)

if not answer:print(-1)
else:
    answer.sort(key=lambda x: (distanceJ[x],x))
    print(answer[0])
    
