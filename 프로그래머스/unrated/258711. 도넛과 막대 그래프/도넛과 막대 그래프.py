from collections import deque

def solution(edges):
    n=0
    answer = [0,0,0,0]
    for edge in edges:
        x,y=edge
        n=max(n,x,y)
    graph=[[] for i in range(n+1)]
    indegree=[0]*(n+1)
    outdegree=[0]*(n+1)
    for edge in edges:
        x,y=edge
        graph[x].append(y)
        outdegree[x]+=1
        indegree[y]+=1
    for i in range(1,n+1):
        if indegree[i]==0 and outdegree[i]>1:
            extra=i
            answer[0]=i
    visited=[0]*(n+1)
    visited[extra]=1
    
    def travel(x):
        q=deque()
        q.append(x)
        visited[x]=1
        isDonut=1
        if outdegree[x]==0: 
            answer[2]+=1
            return
        if not (indegree[x]==1 and outdegree[x]==1):
            isDonut=0
        
        while q:
            now=q.popleft()
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    if outdegree[to]==0:
                        answer[2]+=1
                        return
                    if not (indegree[to]==1 and outdegree[to]==1):
                        isDonut=0
                    q.append(to)
        
        if isDonut:answer[1]+=1
        else: answer[3]+=1
    
    for x in graph[extra]:
        indegree[x]-=1
        travel(x)
    
    return answer