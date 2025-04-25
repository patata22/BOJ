from collections import deque
import sys
input=sys.stdin.readline

def sol(graph,start):
    q=deque()
    q.append(start)
    visited=[-1]*(n+1)
    visited[start]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if visited[to]==-1:
                    visited[to]=t
                    q.append(to)
        t+=1
    return visited

for tt in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    graph_reverse=[[] for i in range(n+1)]

    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph_reverse[b].append(a)
    
    distance1=sol(graph,1)
    distance2=sol(graph_reverse,n)
    short=distance1[n]
    answer=[]
    for i in range(1,n+1):
        if distance1[i]<0 or distance2[i]<0: continue
        if distance1[i]+distance2[i]==short: answer.append(i)

    print(*answer)