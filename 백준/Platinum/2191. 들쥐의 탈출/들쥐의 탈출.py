import sys
input=sys.stdin.readline

def reachable(loc,ca):
    a,b=loc
    c,d=ca
    return (c-a)**2+(d-b)**2<=MAX

def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if used[to]<0 or (not visited[used[to]] and dfs(used[to])):
            used[to]=now
            return 1
    return 0

n,m,s,v=map(int,input().split())
MAX=(v*s)**2
location=[tuple(map(float,input().split())) for i in range(n)]
caves=[tuple(map(float,input().split())) for i in range(m)]
graph=[[] for i in range(n)]
for i in range(n):
    loc=location[i]
    for j in range(m):
        ca=caves[j]
        if reachable(loc,ca): graph[i].append(j)

used=[-1]*(m+1)
answer=0
for i in range(n):
    visited=[0]*(n)
    answer+=dfs(i)
    
print(n-answer)
