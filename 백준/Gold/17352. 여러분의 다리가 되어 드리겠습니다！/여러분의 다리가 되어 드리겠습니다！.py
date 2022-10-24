from collections import deque
import sys
input=sys.stdin.readline

def sol(x):
    q=deque()
    q.append(x)
    while q:
        now = q.popleft()
        for x in graph[now]:
            if not visited[x]:
                visited[x]=1
                q.append(x)

n=int(input())
graph=[[] for i in range(n+1)]
visited=[0]*(n+1)

for _ in range(n-2):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer=[]

for i in range(1,n+1):
    if not visited[i]:
        visited[i]=1
        answer.append(i)
        sol(i)

print(*answer)
