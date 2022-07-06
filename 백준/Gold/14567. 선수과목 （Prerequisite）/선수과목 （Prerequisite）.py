from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    t=2
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            answer[i]=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for x in graph[now]:
                indegree[x]-=1
                if indegree[x]==0:
                    answer[x]=t
                    q.append(x)
        t+=1


n,m=map(int,input().split())

indegree=[0]*(n+1)
answer=[0]*(n+1)
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
sol()
print(*answer[1:])
