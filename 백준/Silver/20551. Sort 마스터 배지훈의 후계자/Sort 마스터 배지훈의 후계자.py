import sys
input=sys.stdin.readline
def lower_bound(x):
    l=-1
    r=n
    while l+1<r:
        mid=(l+r)//2
        if number[mid]<x: l=mid
        else: r=mid
    if r==n or number[r]!=x:return -1
    else: return r
    

n,m=map(int,input().split())
number=[int(input()) for i in range(n)]
number.sort()
for _ in range(m):
    print(lower_bound(int(input())))
