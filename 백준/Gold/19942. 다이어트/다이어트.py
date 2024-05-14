def sol(depth):
    if depth==n:
        global answer,menu
        p,f,s,v,cost=0,0,0,0,0
        lst=[]
        for i in range(n):
            if used[i]:
                P,F,S,V,C=number[i]
                p+=P
                f+=F
                s+=S
                v+=V
                cost+=C
                lst.append(i+1)
        if p>=mp and f>=mf and s>=ms and v>=mv:
            if cost<answer:
                answer=cost
                menu=lst
            elif cost==answer:
                menu=sorted([lst,menu])[0]
                
        return
    
    sol(depth+1)
    used[depth]=1
    sol(depth+1)
    used[depth]=0

n=int(input())
mp,mf,ms,mv = map(int,input().split())
number=[tuple(map(int,input().split())) for i in range(n)]
answer=float('inf')
menu=[]
used=[0]*n

sol(0)
if answer==float('inf'):print(-1)
else:
    print(answer)
    print(*menu)