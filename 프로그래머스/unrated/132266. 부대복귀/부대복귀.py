from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    distance=[-1]*(n+1)
    graph=[[] for i in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    q=deque()
    q.append(destination)
    distance[destination]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if distance[to]<0:
                    distance[to]=t
                    q.append(to)
        t+=1
    return [distance[x] for x in sources]
