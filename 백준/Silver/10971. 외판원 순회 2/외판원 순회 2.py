def sol(now, c,cnt):
    global answer
    if c>answer:return
    if cnt==n:
        if cost[now][0]:
            answer=min(c+cost[now][0],answer)
        return
    for i in range(n):
        if not visited[i] and cost[now][i]:
            visited[i]=1
            sol(i,c+cost[now][i],cnt+1)
            visited[i]=0


n=int(input())
answer=float('inf')
cost=[list(map(int,input().split())) for i in range(n)]
visited=[0]*n
visited[0]=1
sol(0,0,1)
print(answer)

