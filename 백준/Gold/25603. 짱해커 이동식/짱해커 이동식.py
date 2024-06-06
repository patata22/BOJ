def sol():
    l=0
    r=10**9+1
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else: l=mid
    return r

def check(mid):
    now=-1
    for i in range(n):
        if number[i]<=mid:
            if i-now>k: return False
            now=i
    if n-now>k: return False
    return True
    
n,k=map(int,input().split())
number=tuple(map(int,input().split()))
print(sol())
