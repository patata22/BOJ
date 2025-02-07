from collections import deque
import sys
input=sys.stdin.readline

def travel(x):
   q=deque()
   q.append(x)
   visited[x]=1
   while q:
      now=q.popleft()
      for to in graph[now]:
         if not visited[to]:
            visited[to]=1
            q.append(to)

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
   a,b=map(int,input().split())
   graph[a].append(b)
   graph[b].append(a)

odd=0
for i in range(1,n+1):
   if len(graph[i])%2: odd+=1

cnt=0
visited=[0]*(n+1)
for i in range(1,n+1):
   if not visited[i]:
      cnt+=1
      travel(i)

if (odd==2 or odd==0) and cnt==1: print('YES')
else:print('NO')
