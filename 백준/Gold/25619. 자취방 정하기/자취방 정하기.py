import sys,heapq
input=sys.stdin.readline

def sol():
    q=[(0,1)]
    distance=[float('inf')]*(n+1)
    distance[1]=0
    flag=False
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if d<0:
                flag=True
                if distance[to]!=-float('inf'):
                    distance[to]=-float('inf')
                    heapq.heappush(q,(-float('inf'),to))
            else:
                if distance[to]>dist+d:
                    distance[to]=dist+d
                    heapq.heappush(q,(dist+d,to))

    result=[]
    if flag:
        for i in range(2,n+1):
            if distance[i]!=float('inf'): result.append(i)
    else:
        for i in range(2,n+1):
            if distance[i]<=T: result.append(i)
    print(len(result))
    if result:print(*result)


n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c,d=map(int,input().split())
    e=c+d
    graph[a].append((b,e))
    graph[b].append((a,e))
T=int(input())*2

sol()
