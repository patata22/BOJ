def sol():
    l=0
    r=10**10
    while l+1<r:
        mid=(l+r)//2
        total=(mid*(mid+1))//2
        for i in range(1,n):
            gap = day[i-1]-day[i]
            if gap>=mid: total+=(mid*(mid+1))//2
            else:total+=(mid*(mid+1))//2 - (mid-gap)*(mid-gap+1)//2
        if total>=k: r=mid
        else: l= mid
    return r
        

n,k=map(int,input().split())

day=list(map(int,input().split()))[::-1]

print(sol())
         
