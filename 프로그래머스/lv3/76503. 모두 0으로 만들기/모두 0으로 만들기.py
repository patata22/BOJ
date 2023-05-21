import sys
sys.setrecursionlimit(10**6)



def solution(a, edges):
    if sum(a): return -1
    
    answer=0
    graph=[[] for i in range(len(a))]
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)
    visited=[0]*(len(a))
    
    def dfs(now):
        visited[now]=1
        nonlocal answer
        for to in graph[now]:
            if not visited[to]:
                temp=dfs(to)
                a[now]+=temp
                answer+=abs(temp)
        return a[now]
    dfs(0)
    return answer
                
            