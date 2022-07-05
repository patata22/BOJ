import heapq

def sol():
    q=[]
    q.append((0,0))
    while q:
        dist,now = heapq.heappop(q)
        if dist!=distance[now]:continue
        if now==m-1:return True
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                trace[to]=now
                heapq.heappush(q,(dist+d, to))
    return False

for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(m)]
    distance=[float('inf')]*m
    trace=[0]*m
    distance[0]=0
    for __ in range(n):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    print(f'Case #{_+1}:', end=' ')
    if not sol():print(-1)
    else:
        now=m-1
        answer=[]
        while now:
            answer.append(now)
            now=trace[now]
        answer.append(0)
        print(*answer[::-1])
        
              
