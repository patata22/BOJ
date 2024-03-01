import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(now):
    global answer,unused
    unused+=1
    visited[now]=unused
    stack.append(now)
    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result,dfs(to))
        elif not finished[to]: result=min(result, visited[to])
    if result==visited[now]:
        count=0
        while True:
            t=stack.pop()
            finished[t]=1
            count+=1
            if t==now:break
        answer=max(answer,count)
    return result

n,m=int(input()),int(input())
graph=[[] for i in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

visited=[0]*(n+1)
finished=[0]*(n+1)
unused=0
stack=[]
answer=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
print(answer)