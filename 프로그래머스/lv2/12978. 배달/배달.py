import heapq

def solution(N, road, K):
    
    distance=[float('inf')]*(N+1)
    graph=[[] for i in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    q=[(0,1)]
    distance[1]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]!=dist: continue
        for to , d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q, (dist+d, to))
    
    answer=0
    for i in range(1,N+1):
        if distance[i]<=K: answer+=1
    return answer