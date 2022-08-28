def dfs(now, record):
    global answer
    visited[now]=1
    to=number[now]
    if to in record:
        answer+=len(record)-record.index(to)
        for i in range(record.index(to),len(record)):
            cycle.append(record[i])
        return
    else:
        if not visited[to]:
            record.append(to)
            dfs(to,record)


n=int(input())
number=[0]+[int(input()) for i in range(n)]
visited=[0]*(n+1)
answer=0
cycle=[]
for i in range(1,n+1):
    if not visited[i]:
        dfs(i,[i])
print(answer)
cycle.sort()
for x in cycle:print(x)

