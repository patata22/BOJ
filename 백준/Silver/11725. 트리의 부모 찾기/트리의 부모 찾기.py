from collections import deque
import sys
input=sys.stdin.readline
def dfs():
    q=deque()
    q.append(1)
    parent[1]=0
    while q:
        now = q.popleft()
        for x in graph[now]:
            if parent[x]==-1:
                parent[x]=now
                q.appendleft(x)
    

n=int(input())

parent=[-1]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs()

for i in range(2,n+1):
    print(parent[i])
