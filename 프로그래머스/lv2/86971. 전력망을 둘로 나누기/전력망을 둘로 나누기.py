from collections import deque

def solution(n, wires):
    answer = 100
    graph=[[] for i in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(n,cutX, cutY):
        limit=((cutX,cutY), (cutY,cutX))
        q=deque()
        q.append(1)
        visited=[0]*(n+1)
        visited[1]=1
        count=1
        while q:
            now=q.popleft()
            for to in graph[now]:
                if (now,to) in limit:continue
                if not visited[to]: 
                    visited[to]=1
                    q.append(to)
                    count+=1
        return abs(n-2*count)
    
    for x,y in wires:
        answer=min(answer,bfs(n,x,y))
    return answer
