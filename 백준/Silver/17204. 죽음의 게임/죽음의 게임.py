n,k=map(int,input().split())

graph=[int(input()) for i in range(n)]
visited=[0]*(n)
now=0
answer=0
while now!=k:
    answer+=1
    if visited[graph[now]]:break
    visited[graph[now]]=1
    now=graph[now]
if visited[k]:print(answer)
else: print(-1)