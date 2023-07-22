from collections import deque
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
        if not visited[to]: result = min(result, dfs(to))
        elif not finished[to]: result = min(result, visited[to])

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

def makeIndegree():
    q=deque()
    indegree=[0]*scc_cnt
    visited=[0]*scc_cnt
    q.append(scc_num[s])
    visited[scc_num[s]]=1
    while q:
        now=q.popleft()
        scc_now= SCC[now]
        for node in scc_now:
            for to in graph[node]:
                if scc_num[node]!=scc_num[to]:
                    indegree[scc_num[to]]+=1
                    if not visited[scc_num[to]]:
                        visited[scc_num[to]]=1
                        q.append(scc_num[to])
    return indegree

def getCash():
    q=deque()
    q.append(scc_num[s])
    answer=0
    cash=[0]*(scc_cnt+1)
    while q:
        now=q.popleft()
        
        scc_now = SCC[now]
        temp_cash = cash[now]
        flag=False
        for node in scc_now:
            temp_cash+=atm[node]
            if restaurant[node]: flag=True
        if flag:
            answer=max(answer,temp_cash)
        for node in scc_now:
            for to in graph[node]:
                if scc_num[to]!=scc_num[node]:
                    indegree[scc_num[to]]-=1
                    cash[scc_num[to]]=max(cash[scc_num[to]], temp_cash)
                    if indegree[scc_num[to]]==0:
                        q.append(scc_num[to])
    return answer
                    
n,m=map(int,input().split())
graph=[[] for i in range(n)]
for _ in range(m):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[a].append(b)
atm=[int(input()) for i in range(n)]
s,p=map(lambda x: int(x)-1,input().split())
restaurant=[0]*n
for x in map(int,input().split()):
    restaurant[x-1]=1
visited=[0]*n
finished=[0]*n
scc_num=[-1]*n
cnt=0
scc_cnt=-1
SCC=[]
stack=[]

for i in range(n):
    if not visited[i]:
        dfs(i)
scc_cnt+=1
indegree = makeIndegree()
print(getCash())
