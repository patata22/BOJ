def sol(depth,invin,didInvin):
    global H,D,answer
    if depth==n:
        answer=max(answer,H)
        return

    if invin:
        D+=k
        sol(depth+1,False, True)
        D-=k
    else:
        defense=max(0,(damage[depth]-D)//2)
        H-=defense
        if H>0:sol(depth+1,invin,didInvin)
        H+=defense
        D+=k
        walk=max(0,damage[depth]-D)
        H-=walk
        if H>0:sol(depth+1,invin,didInvin)
        H+=walk
        D-=k
        if not didInvin:
            temp=max(0,damage[depth]-D)
            H-=temp
            if H>0: sol(depth+1,True,True)
            H+=temp

n=int(input())
H,D,k=map(int,input().split())
damage=[int(input()) for i in range(n)]
answer=0

sol(0,False,False)

if answer==0: print(-1)
else: print(answer)
