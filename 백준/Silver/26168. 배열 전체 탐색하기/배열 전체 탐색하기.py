import sys
input=sys.stdin.readline

def lower_bound(i):
    l = -1
    r = n
    while l+1<r:
        mid = (l+r)//2
        if not number[mid]>=i: l=mid
        else: r=mid
    return r

def upper_bound(i):
    l = -1
    r = n
    while l+1<r:
        mid = (l+r)//2
        if not number[mid]>i: l = mid
        else: r = mid
    return r

n,m=map(int,input().split())

number = sorted(list(map(int,input().split())))
for _ in range(m):
    temp = list(map(int,input().split()))
    if temp[0]==1:
        print(n-lower_bound(temp[1]))
    elif temp[0]==2:
        print(n-upper_bound(temp[1]))
    else:
        lower = lower_bound(temp[1])
        upper = upper_bound(temp[2])
        print(upper-lower)
    
