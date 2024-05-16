def sol(n):
    l=-1
    r=2**32
    while l+1<r:
        mid=(l+r)//2
        t = mid**2
        if t<n:l=mid
        else: r=mid
    return r
        
print(sol(int(input())))