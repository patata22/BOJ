from collections import deque
import sys
input=sys.stdin.readline

def sol(k,start):
    q=deque()
    q.append((start,float('inf')))
    visited=[0]*(n+1)
    visited[start]=1
    answer=0
    while q:
        now,cost = q.popleft()
        for to,c in graph[now]:
            if not visited[to]:
                visited[to]=1
                C=min(cost,c)
                if C<k: continue
                answer+=1
                q.append((to,C))
    return answer
            
        
        

n,q=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for _ in range(q):
    k,start=map(int,input().split())
    print(sol(k,start))
