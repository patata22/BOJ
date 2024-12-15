def check(x):
    total=0
    while x:
        total+=x//5
        x//=5
    return total

def sol():
    l=-1
    r=500000001
    while l+1<r:
        mid=(l+r)//2
        result=check(mid)
        if result>=n: r=mid
        else: l=mid
    if check(r)==n: return r
    else: return -1
    
n=int(input())
print(sol())

