from collections import deque

def reachable(x,y):
    a,b,c=x
    d,e,f=y
    return ((a-d)**2)+((b-e)**2)<=c

def sol(x):
    q=deque()
    q.append(x)
    visited=[0]*n
    visited[x]=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append(to)
    return sum(visited)
n=int(input())
answer=0
cow=[]
graph=[[] for i in range(n)]
for _ in range(n):
    a,b,c=map(int,input().split())
    cow.append((a,b,c*c))
for i in range(n):
    x=cow[i]
    for j in range(n):
        y=cow[j]
        if reachable(x,y):
            graph[i].append(j)
for i in range(n):
    answer=max(answer,sol(i))
print(answer)