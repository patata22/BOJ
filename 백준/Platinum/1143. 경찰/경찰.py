def scc(now):
    global unused,sccCnt
    unused+=1
    visited[now]=unused
    result=unused
    stack.append(now)

    for to in graph[now]:
        if not visited[to]: result=min(result,scc(to))
        elif not finished[to]: result=min(result,visited[to])

    if result==visited[now]:
        sccCnt+=1
        temp=[]
        while True:
            t=stack.pop()
            finished[t]=1
            sccNum[t]=sccCnt
            temp.append(t)
            if t==now: break
        SCC.append(temp)
    return result

def topSort():
    indegree=[0]*len(SCC)
    for now in range(n):
        for to in graph[now]:
            if sccNum[to]==sccNum[now]: continue
            indegree[sccNum[to]]+=1
    temp=[]
    for i in range(len(SCC)):
        if not indegree[i]: temp.append(i)
    return temp

def calcCost(now):
    S = SCC[now]
    C =float('inf')
    idx=-1
    for x in S:
        if C>cost[x]:
            C=cost[x]
            idx=x
    office[idx]=1
    return C
    
        
n=int(input())
cost=list(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(n):
    temp=list(input())
    for j in range(n):
        if temp[j]=='Y':
            graph[i].append(j)

unused=0
visited=[0]*n
finished=[0]*n
SCC=[]
sccNum=[0]*n
sccCnt=-1
stack=[]

for i in range(n):
    if not visited[i]:
        scc(i)

zero=topSort()
office=[0]*n
totalCost=0
officeCount=0
for z in zero:
    totalCost+=calcCost(z)
    officeCount+=1
leftCost=[]
for i in range(n):
    if not office[i]: leftCost.append(cost[i])
leftCost.sort()
for x in leftCost:
    if totalCost*(officeCount+1)>(totalCost+x)*officeCount:
        totalCost+=x
        officeCount+=1
    else: break
print(totalCost/officeCount)