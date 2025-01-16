def sol(now,time,depth):
    global answer

    if now%2:temp=distance[now][now-1]
    else: temp=distance[now][now+1]

    if depth==5:
        answer=min(answer,time+temp)
        return
    
    for i in range(12):
        if not visited[i//2]:
            visited[i//2]=1
            if now%2:dist=distance[now-1][i]
            else: dist=distance[now+1][i]
            sol(i,time+temp+dist,depth+1)
            visited[i//2]=0

distance=[list(map(int,input().split())) for i in range(12)]
visited=[0]*6
answer=float('inf')

for i in range(12):
    visited[i//2]=1
    sol(i,0,0)
    visited[i//2]=0

print(answer)
