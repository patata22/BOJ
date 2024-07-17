def check(mid):
    total=0
    for t in tree:
        if t>mid: total+=t-mid
    return total>=m
def sol():
    l=-1
    r=1000000000
    while l+1<r:
        mid=(l+r)//2
        if check(mid): l=mid
        else: r=mid
    return l
        
n,m=map(int,input().split())
tree=tuple(map(int,input().split()))
print(sol())
