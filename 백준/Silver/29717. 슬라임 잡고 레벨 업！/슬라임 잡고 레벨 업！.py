import sys
input=sys.stdin.readline

def sol(n):
    total = n*(n+1)//2
    l=0
    r=10**9
    while l+1<r:
        mid=(l+r)//2
        if mid*(mid+1)<=total:l=mid
        else:r=mid
    return l+1


for tt in range(int(input())):
    print(sol(int(input())))
