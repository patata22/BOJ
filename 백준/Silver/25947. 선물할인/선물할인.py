def sol():
    l=0
    r=n+1
    while l+1<r:
        mid=(l+r)//2
        if mid<=a:
            total=cost[mid]//2
        else:
            total=cost[mid-a]+(cost[mid]-cost[mid-a])//2
        if total>b: r=mid
        else: l=mid

    return l

n,b,a=map(int,input().split())

cost=list(map(int,input().split()))
cost.append(0)
cost.sort()
for i in range(1,n+1):
    cost[i]+=cost[i-1]

print(sol())
