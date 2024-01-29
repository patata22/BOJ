def dfs(now):
    visited[now]=1
    nxt=number2[now]
    if visited[nxt] and not finished[nxt]:
        answer.append(nxt)
        while nxt!=now:
            nxt=number2[nxt]
            answer.append(nxt)       
    else:
        if not visited[nxt]:
            dfs(nxt)
    finished[now]=1

n=int(input())
number=[i for i in range(n+1)]
number2=[0]
for _ in range(n):
    number2.append(int(input()))
visited=[0]*(n+1)
finished=[0]*(n+1)
answer=[]
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
answer.sort()
print(len(answer))
print(*answer,sep='\n')
