from collections import deque
import sys
input=sys.stdin.readline

def makeFlow(n):
    if n==1: return
    flow[p[n]][n]+=1
    flow[n][p[n]]-=1
    makeFlow(p[n])

n,p=map(int,input().split())
capacity = [[0]*(2*n+1) for i in range(2*n+1)]
flow = [[0]*(2*n+1) for i in range(2*n+1)]
graph = [[] for i in range(2*n+1)]
answer=0
for i in range(1,n+1):
    capacity[i][i+n]=1
    capacity[i+n][i]=1
    graph[i].append(i+n)

capacity[1][1+n]=float('inf')

for i in range(p):
    a,b= map(int,input().split())
    graph[a+n].append(b)
    graph[b].append(a+n)
    capacity[a+n][b]=1
    graph[b+n].append(a)
    graph[a].append(b+n)
    capacity[b+n][a]=1
    

while True:
    p=[-1]*(2*n+1)
    q=deque()
    q.append(1)
    while q:
        now=q.popleft()
        for to in graph[now]:
            if capacity[now][to]-flow[now][to]>0 and p[to]==-1:
                p[to]=now
                q.append(to)
    
    if p[2]==-1: break
    makeFlow(2)
    answer+=1

print(answer)