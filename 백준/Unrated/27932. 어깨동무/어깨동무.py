n,k=map(int,input().split())

height=tuple(map(int,input().split()))

l=-1
r=max(height)-min(height)+1
if n==1: print(0)
else:
    while l+1<r:
        mid=(l+r)//2
        count=0
        if abs(height[0]-height[1])>mid:count+=1
        for i in range(1,n-1):
            if abs(height[i]-height[i-1])>mid or abs(height[i]-height[i+1])>mid: count+=1
        if abs(height[-1]-height[-2])>mid:count+=1
        if count<=k: r=mid
        else: l=mid
    print(r)
