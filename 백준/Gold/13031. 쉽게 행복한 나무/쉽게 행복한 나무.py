import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(now,cost):
    visited[now]=1
    result=0
    total=1
    for to,c in graph[now]:
        if visited[to]:continue
        son,needDel=sol(to,cost+c)
        result+=needDel
        total+=son
    if number[now]<cost:
        return (total,total)
    else: return (total,result)
          
n=int(input())
number=[0]+list(map(int,input().split()))
graph=[[] for i in range(n+1)]
for now in range(2,n+1):
    to,cost=map(int,input().split())
    graph[now].append((to,cost))
    graph[to].append((now,cost))
visited=[0]*(n+1)

print(sol(1,0)[1])