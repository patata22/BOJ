bomb=[tuple(map(int,input().split())) for i in range(int(input()))]
bomb.sort(reverse = True)

T=bomb[0][0]

distance=[float('inf')]*2001
distance[0]=0
for t in range(1,T+1):
    nxt = [float('inf')]*2001
    for i in range(-1000,1001):
        if -1000<=i-1<=1000:
            nxt[i-1]=min(nxt[i-1],distance[i]+1)
        nxt[i]=min(nxt[i],distance[i])
        if -1000<=i+1<=1000:
            nxt[i+1]=min(nxt[i+1],distance[i]+1)
    
    if t==bomb[-1][0]:    
        _,a,b=bomb.pop()
        for i in range(a+1,b):
            nxt[i]=float('inf')
    distance=nxt

answer=min(distance)
if answer==float('inf'):print(-1)
else:print(answer)
