def choice(depth):
    if depth==6:
        bid()
        return
    used[depth]=1
    choice(depth+1)
    used[depth]=0
    choice(depth+1)

def bid():
    ret=0
    total=k
    for x in number:
        if used[x]:
            if cost[x]>total: break
            ret+=1
            total-=cost[x]
            
    global answer
    answer=max(answer,ret)
        

n,k=map(int,input().split())
cost=tuple(map(int,input().split()))
number=list(map(lambda x:int(x)-1, input().split()))
answer=0
used=[0]*6

choice(0)
print(answer)