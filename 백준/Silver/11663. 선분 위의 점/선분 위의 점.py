import sys
input= sys.stdin.readline

def lower_bound(i):
    l = -1
    r = n
    while l+1<r:
        mid = (l+r)//2
        if not point[mid]>=i: l=mid
        else: r=mid
    return r

def upper_bound(i):
    l = -1
    r = n
    while l+1<r:
        mid = (l+r)//2
        if not point[mid]>i: l=mid
        else: r=mid
    return r

n,m = map(int,input().split())
point = sorted(list(map(int,input().split())))
for _ in range(m):
    s,e = map(int,input().split())
    print(upper_bound(e)-lower_bound(s))
