import sys
input=sys.stdin.readline

def upper_bound(i):
    l=-1
    r=n
    while l+1<r:
        mid = (l+r)//2
        if not criteria[mid]>=i: l=mid
        else: r = mid
    if r==n: return name[r-1]
    return name[r]

n,m = map(int,input().split())
name = []
criteria = []

for _ in range(n):
    na,c = input().split()
    name.append(na)
    criteria.append(int(c))

for _ in range(m):
    print(upper_bound(int(input())))
