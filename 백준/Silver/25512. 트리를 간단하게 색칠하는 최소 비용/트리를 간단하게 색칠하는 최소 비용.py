from collections import deque
import sys
input=sys.stdin.readline

def sol(color):
    q=deque()
    q.append((0,color))
    visited=[0]*n
    visited[0]=1
    c=cost[0][color]
    
    while q:
        now, color= q.popleft()
        nxt_color=1-color
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append((to,nxt_color))
                c+=cost[to][nxt_color]
    return c
                
            
            
    
n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cost=[tuple(map(int,input().split())) for i in range(n)]

print(min(sol(0),sol(1)))
