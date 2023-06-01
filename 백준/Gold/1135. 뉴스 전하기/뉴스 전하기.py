def sol(now):
    visited[now]=1
    if not graph[now]: return 1
    time=[]
    for to in graph[now]:
        if not visited[to]:
            time.append(sol(to))
    time.sort(reverse=True)
    for i in range(len(time)):
        time[i]+=i
    return max(time)+1
    

n=int(input())
number=tuple(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(1,n):
    graph[number[i]].append(i)
visited=[0]*n


print(sol(0)-1)
