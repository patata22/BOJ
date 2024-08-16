from collections import deque

def sol():
    q=deque()
    temp=input().split()
    for x in temp[1:]:
        q.append(ord(x)-65)
        indegree[ord(x)-65]=0
    while q:
        now=q.popleft()
        for to in graph[now]:
            indegree[to]-=1
            if indegree[to]==0:
                q.append(to)
    return n-indegree.count(0)

n,m=map(int,input().split())
graph=[[] for i in range(n)]
indegree=[0]*n
for _ in range(m):
    a,b=map(lambda x: ord(x)-65, input().split())
    graph[a].append(b)
    indegree[b]+=1

print(sol())

