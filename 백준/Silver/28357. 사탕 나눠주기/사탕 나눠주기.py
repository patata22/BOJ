def sol():
    l=-1
    r=max(number)
    while l+1<r:
        mid=(l+r)//2
        count=0
        for x in number:
            count+=max(0,x-mid)
        if count<=k: r=mid
        else: l=mid
    return r

n,k=map(int,input().split())
number=list(map(int,input().split()))
print(sol())
