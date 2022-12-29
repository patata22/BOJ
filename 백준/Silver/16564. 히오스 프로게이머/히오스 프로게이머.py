import sys
input=sys.stdin.readline

n,k = map(int,input().split())
level = [int(input()) for i in range(n)]

l=1
r=2000000000
while l+1<r:
    mid = (l+r)//2
    count=0
    for lev in level:
        if mid>lev: count+=mid-lev
    if count<=k: l= mid
    else: r= mid
print(l)
