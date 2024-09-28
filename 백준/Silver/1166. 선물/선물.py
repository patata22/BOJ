def sol():
    l=0
    r=min(L,W,H)+1
    for i in range(100):
        mid=(l+r)/2
        cnt=(L//mid)*(W//mid)*(H//mid)
        if cnt>=n: l=mid
        else: r=mid
    return l

n,L,W,H=map(int,input().split())

print(sol())
