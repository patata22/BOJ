import sys
input=sys.stdin.readline

def upper_bound(i):
    l = -1
    r = n
    while l+1<r:
        mid = (l+r)//2
        if not A[mid]>i: l = mid
        else: r = mid
    return r

for _ in range(int(input())):
    n,m=map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = tuple(map(int,input().split()))
    answer=0
    for b in B:
        answer+=(n-upper_bound(b))
    print(answer)
