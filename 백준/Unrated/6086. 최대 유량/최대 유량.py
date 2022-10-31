from collections import deque


def findMin(n):
    global minFlow
    if n==start: return
    rest = capacity[p[n]][n]-flow[p[n]][n]
    minFlow=min(rest,minFlow)
    findMin(p[n])

def makeFlow(n):
    if n==start: return
    flow[p[n]][n]+=minFlow
    flow[n][p[n]]-=minFlow
    makeFlow(p[n])
    
n=int(input())
graph = [[] for i in range(52)]
toNumber={}
cnt=0
capacity = [[0]*52 for i in range(52)]
flow = [[0]*52 for i in range(52)]
answer=0
for _ in range(n):
    a,b,c=input().split()
    if a not in toNumber:
        toNumber[a]=cnt
        cnt+=1
    if b not in toNumber:
        toNumber[b]=cnt
        cnt+=1
    a=toNumber[a]
    b=toNumber[b]
    c=int(c)
    capacity[a][b]+=c
    capacity[b][a]+=c
    graph[a].append(b)
    graph[b].append(a)
start=toNumber['A']
end=toNumber['Z']
    
while True:
    p=[-1]*52
    q=deque()
    q.append(start)
    while q:
        now=q.popleft()
        for to in graph[now]:
            if capacity[now][to]-flow[now][to]>0 and p[to]==-1:
                q.append(to)
                p[to]=now
    if p[toNumber['Z']]==-1:break

    minFlow=float('inf')
    findMin(end)
    makeFlow(end)
    answer+=minFlow

print(answer)
