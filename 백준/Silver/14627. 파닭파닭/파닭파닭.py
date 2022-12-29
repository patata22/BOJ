import sys
input=sys.stdin.readline

s,c=map(int,input().split())

pa = [int(input()) for i in range(s)]

l=1
r=max(pa)

while l<=r:
    mid=(l+r)//2
    count=0
    for p in pa:
        count+=p//mid
    if count>=c: l=mid+1
    else: r= mid-1

print(sum(pa)-c*r)
