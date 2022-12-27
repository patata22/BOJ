from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)

apple = list(map(int,input().split()))

q=deque()
q.append(0)
answer=apple[0]
t=0
while q and t<k:
    for _ in range(len(q)):
        now = q.popleft()
        for to in graph[now]:
            answer+=apple[to]
            q.append(to)
    t+=1
print(answer)
