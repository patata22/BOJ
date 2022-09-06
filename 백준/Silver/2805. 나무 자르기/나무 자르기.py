n,m=map(int,input().split())
tree=list(map(int,input().split()))
l=0
r=2000000001
while l+1<r:
    
    mid=(l+r)//2
    temp=0
    for x in tree:
        temp+=max(x-mid,0)
    if temp>=m:
        l=mid
    else: r=mid
print(l)