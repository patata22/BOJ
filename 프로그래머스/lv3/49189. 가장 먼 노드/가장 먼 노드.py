from collections import deque

def solution(n, vertex):
    
    graph=[[] for i in range(n+1)]
    for a,b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    visited=[0]*(n+1)
    
    q=deque()
    q.append(1)
    visited[1]=1
    while q:
        answer=len(q)
        for _ in range(answer):
            now=q.popleft()
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    q.append(to)
    return answer