def sol(depth):
    global answer
    if depth==m:
        temp=set()
        for i in range(m):
            if used[i]:
                for x in mate[i]:
                    temp.add(x)
        if len(temp)==n: answer=min(answer,sum(used))
        return
    used[depth]=1
    sol(depth+1)
    used[depth]=0
    sol(depth+1)
    
n,m=map(int,input().split())
mate = [list(map(int,input().split()))[1:] for i in range(m)]
used=[0]*m
answer=float('inf')
sol(0)
print(-1) if answer==float('inf') else print(answer)