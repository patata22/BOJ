import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph= [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

cycle= False
distance= [float('inf')]*(n+1)
distance[1] = 0
for i in range(n):
    for j in range(1,n+1):
        for to,d in graph[j]:
            if distance[to]>distance[j]+d:
                distance[to] = distance[j] + d
                if i==n-1: cycle = True

if cycle: print(-1)
else:
    for i in range(2,n+1):
        print(distance[i]) if distance[i]!=float('inf') else print(-1)
