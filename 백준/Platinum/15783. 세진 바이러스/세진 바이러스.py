import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5+10)

#scc로 묶고 위상정렬

def sol(now):
    global unused,scc_cnt
    unused+=1
    visited[now]=unused
    stack.append(now)

    result=unused
    for to in graph[now]:
        if not visited[to]: result = min(result,sol(to))
        elif not finished[to]: result=min(result,visited[to])

    if result==visited[now]:
        scc_cnt+=1
        scc=[]
        while True:
            t=stack.pop()
            finished[t]=1
            scc.append(t)
            scc_num[t]=scc_cnt
            if t==now: break
        SCC.append(scc)

    return result

def topsort():
    indegree=[0]*len(SCC)
    for i in range(n):
        for to in graph[i]:
            if scc_num[i] == scc_num[to]: continue
            
            indegree[scc_num[to]]+=1
    answer=0
    for x in indegree:
        if not x: answer+=1
    return answer
            

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    

visited=[0]*n
finished=[0]*n
scc_num=[0]*n
unused=0
scc_cnt=-1
stack=[]
SCC=[]

for i in range(n):
    if not visited[i]:
        sol(i)
print(topsort())


