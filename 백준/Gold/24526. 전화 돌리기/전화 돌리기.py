from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    answer=0
    for i in range(1,n+1):
        if not indegree[i]:
            answer+=1
            q.append(i)
    while q:
        now=q.popleft()
        for to in graph[now]:
            indegree[to]-=1
            if not indegree[to]:
                q.append(to)
                answer+=1
    return answer
        

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
indegree=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    indegree[a]+=1
    graph[b].append(a)

print(sol())