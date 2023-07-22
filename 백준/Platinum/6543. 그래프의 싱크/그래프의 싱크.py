import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(now):
    global cnt, scc_cnt
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result = visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result,dfs(to))
        elif not finished[to]: result= min(result, visited[to])

    if result==visited[now]:
        scc=[]
        scc_cnt+=1
        while True:
            t=stack.pop()
            finished[t]=1
            scc.append(t)
            scc_num[t]=scc_cnt
            if t==now: break
        SCC.append(scc)
    return result

def checkOutdegree(num):
    scc=SCC[num]
    flag=True
    for now in scc:
        for to in graph[now]:
            if scc_num[now]!=scc_num[to]:
                return
    for node in scc:
        answer.append(node)

while True:
    x=input()
    if x=='0\n': break
    n,m=map(int,x.split())
    graph=[[] for i in range(n+1)]
    x=tuple(map(int,input().split()))
    for i in range(0,2*m,2):
        a,b=x[i],x[i+1]
        graph[a].append(b)
    cnt=0
    visited=[0]*(n+1)
    finished=[0]*(n+1)
    stack=[]
    SCC=[]
    scc_cnt=-1
    scc_num=[0]*(n+1)

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
    scc_cnt+=1
    answer=[]
    for i in range(scc_cnt):
        checkOutdegree(i)
    answer.sort()
    if answer: print(*answer)
    else: print()