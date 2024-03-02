from collections import deque

def getNum(x):
    global name
    if x not in nameToNum:
        name+=1
        nameToNum[x]=name
    return nameToNum[x]

def makeSCC(now):
    global unused,sccCnt
    unused+=1
    visited[now]=unused
    result=unused
    stack.append(now)

    for to in graph[now]:
        if not visited[to]: result=min(result,makeSCC(to))
        elif not finished[to]: result=min(result, visited[to])

    if result==visited[now]:
        scc=[]
        sccCnt+=1
        while True:
            t=stack.pop()
            finished[t]=1
            scc.append(t)
            sccNum[t]=sccCnt
            if t==now: break
        SCC.append(scc)
    return result

def topSort():
    indegree=[0]*(sccCnt+1)
    for now in range(name+1):
        for to in graph[now]:
            if sccNum[now]==sccNum[to]: continue
            indegree[sccNum[to]]+=1

    q=deque()
    for i in range(sccCnt+1):
        if not indegree[i]:
            q.append(i)

    while q:
        scc=SCC[q.popleft()]
        for now in scc:
            for to in graph[now]:
                if sccNum[now]==sccNum[to]: continue
                indegree[sccNum[to]]-=1
                if indegree[sccNum[to]]==0:
                    q.append(sccNum[to])
                score[to]+=score[now]
                
nameToNum={}
name=-1
n=int(input())
graph=[[] for i in range(1500)]

for _ in range(n):
    temp=input().split()
    end=getNum(temp[0])
    for x in temp[2:]:
        start=getNum(x)
        graph[start].append(end)
visited=[0]*(name+1)
finished=[0]*(name+1)
stack=[]
SCC=[]
sccCnt=-1
unused=0
sccNum=[0]*(name+1)

for i in range(name+1):
    if not visited[i]:
        makeSCC(i)

score=[1]*(name+1)
topSort()
print(score[getNum(input())])