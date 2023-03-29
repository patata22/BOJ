from collections import deque

def solution(n, path, order):
    
    graph=[[] for i in range(n)]
    indegree= [0]*n
    for a,b in path:
        graph[a].append(b)
        graph[b].append(a)
    outdegree={}
    for a,b  in order:
        indegree[b]+=1
        if a not in outdegree: outdegree[a]=[b]
        else: outdegree[a].appned(b)
    if indegree[0]: return False
    def bfs():
        q=deque()
        visited=[0]*(n+1)
        visited[0]=1
        wait=set()
        q.append(0)
        count=1
        while q:
            now = q.popleft()
            if now in outdegree:
                for ins in outdegree[now]:
                    indegree[ins]-=1
                    if not indegree[ins] and ins in wait:
                        visited[ins]=1
                        count+=1
                        wait.remove(ins)
                        q.append(ins)
            for to in graph[now]:
                if not visited[to]:
                    if not indegree[to]:
                        visited[to]=1
                        q.append(to)
                        count+=1
                    elif indegree[to]:
                        wait.add(to)
        return count==n
    return bfs()