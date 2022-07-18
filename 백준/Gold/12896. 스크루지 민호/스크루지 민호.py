from collections import deque
import sys
input=sys.stdin.readline


def sol(X):
    q=deque()
    q.append(X)
    visited={}
    visited[X]=1
    t=1
    cnt=1
    while q:
        for _ in range(len(q)):
            
            now=q.popleft()
            for x in graph[now]:
                if x not in visited:
                    cnt+=1
                    visited[x]=1
                    q.append(x)
                    if cnt==n:
                        return(x,t)
        t+=1
        
n=int(input())
graph=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

far1= sol(1)[0]
answer= (sol(far1)[1]+1)//2
print(answer)
