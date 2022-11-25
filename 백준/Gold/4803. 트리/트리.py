from collections import deque
import sys
input=sys.stdin.readline


def dfs(child,parent):
    tree=1
    q=deque()
    q.append(child)
    visited[child]=1
    while q:
        now = q.popleft()
        for c in graph[now]:
            if c==parent: continue
            elif visited[c]:
                tree=0
                break
            elif not dfs(c,child):
                tree=0
                break
    return tree

t=0
while True:
    t+=1
    n,m=map(int,input().split())
    if n==m==0:break
    else:
        graph=[[] for i in range(n+1)]
        visited=[0]*(n+1)
        answer=0
        for i in range(m):
            a,b=map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)
        for i in range(1,n+1):
            if visited[i]==0:
                answer+=dfs(i,0)
        if answer>1:print(f'Case {t}: A forest of {answer} trees.')
        elif answer==1: print(f'Case {t}: There is one tree.')
        else: print(f'Case {t}: No trees.')
            
