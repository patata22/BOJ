def check(mid):
    temp=0
    for x in time:
        temp+=mid//x
    if temp>=m:return True
    else:return False


n,m=map(int,input().split())
time=list(map(int,input().split()))
l=0
r=10**12+1

while l+1<r:
    mid=(l+r)//2
    if check(mid):r=mid
    else:l=mid
print(r)
