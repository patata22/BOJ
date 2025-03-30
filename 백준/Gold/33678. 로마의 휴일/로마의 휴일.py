def sol():
    if sum(number)*x<k: return -1    
    l=0
    r=n
    while l+1<r:
        mid=(l+r)//2
        if check(n-mid): r=mid
        else: l=mid
    if r==n: return -1
    else: return n-r
    
def check(mid):
    result=0
    for i in range(mid,n): result+=number[i]
    if result>=k: return True
    l=0
    r=mid-1
    while r+1<n:
        r+=1
        result-=number[r]
        result+=x*number[l]
        l+=1
        if result>=k: return True
    
    return False
        
n,k,x=map(int,input().split())
number=tuple(map(int,input().split()))
print(sol())