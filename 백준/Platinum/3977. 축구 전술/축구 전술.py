import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    global cnt, scc_cnt
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result,dfs(to))
        elif not finished[to]: result=min(result, visited[to])

    if result==visited[now]:
        scc=[]
        while True:
            t=stack.pop()
            finished[t]=1
            scc.append(t)
            scc_num[t]=scc_cnt
            if t==now: break
        SCC.append(scc)
        scc_cnt+=1
        
    return result

TT=int(input())
for T in range(TT):
    if T:input()
    n,m=map(int,input().split())
    graph=[[] for i in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
    visited=[0]*n
    finished=[0]*n
    stack=[]
    cnt=0
    scc_cnt=0
    scc_num=[0]*n
    SCC=[]

    for i in range(n):
        if not visited[i]:
            dfs(i)
    indegree=[0]*scc_cnt
    for scc in SCC:
        for now in scc:
            for to in graph[now]:
                if scc_num[now]!=scc_num[to]:
                    indegree[scc_num[to]]+=1

    zero=0
    answer=[]
    for i in range(scc_cnt):
        if not indegree[i]:
            zero+=1
            answer=SCC[i]
    if zero==1:
        answer.sort()
        for x in answer:
            print(x)
    else: print('Confused')
    if T!=TT-1:print()
    
