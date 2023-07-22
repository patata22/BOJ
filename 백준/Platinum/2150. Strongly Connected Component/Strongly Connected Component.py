import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(now):
    global cnt,sccCnt
    cnt+=1
    dfsn[now]=cnt
    stack.append(now)

    result=cnt
    for to in graph[now]:
        if not dfsn[to]:
            result = min(result,dfs(to))
        elif not finished[to]: result = min(result, dfsn[to])

    if result==dfsn[now]:
        scc=[]
        while True:
            t=stack.pop()
            scc.append(t)
            finished[t]=1
            sccNum[t]=sccCnt
            if t==now: break
        scc.sort()
        scc.append(-1)
        SCC.append(scc)
        sccCnt+=1
    return result
    
v,e=map(int,input().split())
cnt=0
sccCnt=0
graph= [[] for i in range(v+1)]
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
dfsn=[0]*(v+1)
sccNum=[-1]*(v+1)
finished=[0]*(v+1)
stack=[]
SCC=[]

for i in range(1,v+1):
    if not dfsn[i]: dfs(i)
SCC.sort()
print(sccCnt)
for scc in SCC: print(*scc)