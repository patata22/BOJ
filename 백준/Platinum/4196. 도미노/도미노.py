import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    global cnt,scc_cnt
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result,dfs(to))
        elif not finished[to]: result=min(result, visited[to])

    if result==visited[now]:
        scc=[]
        scc_cnt+=1
        while True:
            t=stack.pop()
            scc_num[t]=scc_cnt
            finished[t]=1
            scc.append(t)
            if t==now: break
        SCC.append(scc)
    return result

def findSccGraph(scc):
    scc_num_now = scc_num[scc[0]]
    for node in scc:
        for to in graph[node]:
            if scc_num[to]!=scc_num_now:
                scc_graph[scc_num_now].add(scc_num[to])
            
for t in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
    stack=[]
    visited=[0]*(n+1)
    finished=[0]*(n+1)
    scc_num = [0]*(n+1)
    cnt=0
    scc_cnt=0
    SCC=[]

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)

    indegree=[0]*(scc_cnt+1)
    for now in range(1,n+1):
        for to in graph[now]:
            if scc_num[now]!=scc_num[to]:
                indegree[scc_num[to]]+=1
    answer=0
    for i in range(1,scc_cnt+1):
        if not indegree[i]: answer+=1
    print(answer)