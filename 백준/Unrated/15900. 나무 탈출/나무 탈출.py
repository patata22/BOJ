from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

q=deque()
q.append(1)
visited[1]=1
t=1
while q:
    for _ in range(len(q)):
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=t
                q.append(to)
    t+=1

total=0
for i in range(2,n+1):
    if len(graph[i])==1: total+=visited[i]

print('Yes') if total%2 else print('No')

