import sys
input=sys.stdin.readline

def sol():
    l=-1
    r=1000000001
    while l+1<r:
        mid=(l+r)//2
        if para(mid):r=mid
        else:l=mid
    return r

def para(mid):
    count=1
    now = house[0]
    for i in range(1,n):
        to = house[i]
        if to-now>mid:
            count+=1
            now=to
    return count<c


n,c=map(int,input().split())
house=sorted([int(input()) for i in range(n)])

print(sol())
