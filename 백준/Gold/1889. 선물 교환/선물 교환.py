from collections import deque
import sys
input=sys.stdin.readline


def sol():
    q=deque()
    for i in range(n):
        if indegree[i]<2:
            visited[i]=1
            q.append(i)
    while q:
        now=q.popleft()
        for to in graph[now]:
            indegree[to]-=1
            if indegree[to]<2 and not visited[to]:
                visited[to]=1
                q.append(to)

n=int(input())
graph=[[] for i in range(n)]
indegree=[0]*n

for i in range(n):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[i].append(a)
    graph[i].append(b)
    indegree[a]+=1
    indegree[b]+=1

visited=[0]*n

sol()
answer=[]
for i in range(n):
    if indegree[i]==2: answer.append(i+1)

print(len(answer))
if answer:print(*answer)
