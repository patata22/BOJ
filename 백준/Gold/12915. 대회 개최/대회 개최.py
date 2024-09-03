def search(x):
    emm,mhh=em,mh
    if e<x:
        if emm>=x-e:
            emm-=x-e
        else: return False
    if h<x:
        if mhh>=x-h:
            mhh-=x-h
        else: return False
    return m+emm+mhh>=x

e,em,m,mh,h=map(int,input().split())

l=0
r=1000000
while l+1<r:
    mid=(l+r)//2
    if search(mid): l=mid
    else: r= mid
print(l)