def sol():
    l=-1
    r=10000
    while l+1<r:
        mid=(l+r)//2
        minimum=float('inf')
        maximum=-float('inf')
        count=1
        for x in number:
            minimum=min(minimum,x)
            maximum=max(maximum,x)
            if maximum-minimum>mid:
                count+=1
                maximum=x
                minimum=x
        if count<=m: r=mid
        else:l=mid
    return r
n,m=map(int,input().split())
number=list(map(int,input().split()))
print(sol())
