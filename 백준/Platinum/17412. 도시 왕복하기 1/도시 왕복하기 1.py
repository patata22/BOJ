from collections import deque
import sys
input=sys.stdin.readline

START=1
END=2

def sol():
    total=0
    while True:
        prev=[-1]*(n+1)
        q=deque()
        q.append(1)
        while q:
            now=q.popleft()
            for to in graph[now]:
                if capa[now][to]>0 and prev[to]<0:
                    prev[to]=now
                    q.append(to)
            if prev[END]>0: break
        if prev[END]<0: break

        now=END
        while now!=START:
            capa[prev[now]][now]-=1
            capa[now][prev[now]]+=1
            now=prev[now]
        total+=1
    return total

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
capa=[[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    capa[a][b]=1
print(sol())    