def check(mid):
    temp=1
    now=0
    for x in time:
        if x>mid: return float('inf')
        if now+x>mid:
            temp+=1
            now=x
        else: now+=x
    return temp

n,m=map(int,input().split())
time=list(map(int,input().split()))
answer=float('inf')

l=0
r=10**9+1
while l+1<r:
    mid=(l+r)//2
    temp=check(mid)
    if temp>m:l=mid
    else:r=mid
print(r)
