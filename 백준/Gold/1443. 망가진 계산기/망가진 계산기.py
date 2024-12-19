def sol(depth,value):
    if depth==p:
        global answer
        answer=max(answer,value)
        return
    for i in range(2,10):
        temp=value*i
        if temp>=MAX:break
        if (depth+1,temp) not in visited:
            visited.add((depth+1,temp))
            sol(depth+1,temp)

D,p=map(int,input().split())
MAX=10**D
visited=set()
answer=-1

sol(0,1)
print(answer)
