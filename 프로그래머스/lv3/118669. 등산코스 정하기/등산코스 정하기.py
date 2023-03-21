import heapq

def solution(n, paths, gates, summits):
    summits=set(summits)
    graph=[[] for i in range(n+1)]
    for a,b,c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance=[float('inf')]*(n+1)
    q=[]
    for gate in gates:
        q.append((0,gate))
        distance[gate]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist or now in summits: continue
        for to,d in graph[now]:
            temp=max(dist,d)
            if distance[to]>temp:
                distance[to]=temp
                heapq.heappush(q,(temp,to))
    
    answer = float('inf')
    peek=0
    for summit in summits:
        if distance[summit]<answer:
            peek=summit
            answer=distance[summit]
        elif distance[summit]==answer: peek=min(peek,summit)
    return peek,distance[peek]