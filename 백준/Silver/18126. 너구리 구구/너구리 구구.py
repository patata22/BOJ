from collections import deque

def sol():
    q=deque()
    q.append(1)
    distance[1]=0
    while q:
        now=q.popleft()
        for to,d in graph[now]:
            if distance[to]<0:
                distance[to]=distance[now]+d
                q.append(to)
    return max(distance)

n=int(input())
distance=[-1]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

print(sol())