def search(x):
    l=-1
    r=len(dp)
    while l+1<r:
        mid=(l+r)//2
        if dp[mid]<x: l=mid
        else: r=mid
    return r

n=int(input())
number=tuple(map(int,input().split()))
dp=[number[0]]

for i in range(1,n):
    x=number[i]
    if x>dp[-1]: dp.append(x)
    else:
        idx=search(x)
        dp[idx]=x

print(n-len(dp))
   