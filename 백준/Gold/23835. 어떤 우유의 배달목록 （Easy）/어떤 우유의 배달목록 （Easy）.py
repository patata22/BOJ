import sys
input=sys.stdin.readline
from collections import deque

def travel(x,y):
    q=deque()
    q.append(x)
    visited=[0]*(n+1)
    prev=[0]*(n+1)
    visited[x]=1
    t=-1
    flag=False
    while q:
        if flag:break
        for _ in range(len(q)):
            now=q.popleft()
            if now==y:
                flag=True
                break
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    prev[to]=now
                    q.append(to)
        t+=1
    while now!=x:
        answer[now]+=t
        now=prev[now]
        t-=1

n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer=[0]*(n+1)

for _ in range(int(input())):
    cmd=list(map(int,input().split()))
    if cmd[0]==1: travel(cmd[1],cmd[2])
    else: print(answer[cmd[1]])
