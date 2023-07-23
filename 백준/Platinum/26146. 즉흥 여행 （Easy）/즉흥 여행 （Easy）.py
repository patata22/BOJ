import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    global cnt,SCC
    cnt+=1
    visited[now]=cnt
    stack.append(now)

    result=visited[now]
    for to in graph[now]:
        if not visited[to]: result=min(result,dfs(to))
        elif not finished[to]: result=min(result, visited[to])

    if result==visited[now]:
        SCC+=1
        while True:
            t=stack.pop()
            finished[t]=1
            if t==now: break
    
    return result
            
    
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
visited=[0]*(n+1)
finished=[0]*(n+1)
stack=[]
SCC=0
cnt=0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
print('Yes') if SCC==1 else print('No')
