import sys
input=sys.stdin.readline

n,m=map(int,input().split())
jewel = [int(input()) for i in range(m)]

l,r=1,max(jewel)
while l+1<r:
    count=0
    mid = (l+r)//2
    for j in jewel:
        if j%mid==0: count+=(j//mid)
        else: count+=(j//mid)+1
    if count>n: l = mid
    else: r = mid

print(r)
        