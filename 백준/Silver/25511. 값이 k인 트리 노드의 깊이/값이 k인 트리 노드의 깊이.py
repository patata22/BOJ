import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(now,depth):
    if number[now]==k:
        print(depth)
        return
    for to in graph[now]:
        if not visited[to]:
            visited[to]=1
            sol(to,depth+1)


n,k=map(int,input().split())
graph=[[] for i in range(n)]
visited=[0]*n

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

number=tuple(map(int,input().split()))

visited[0]=1
sol(0,0)
