def sol():
    l=0
    r=L
    while l+1<r:
        mid=(l+r)//2
        if check(mid):r=mid
        else:l=mid
    return r

def check(b):
    count=0
    now=0
    energy=b
    for i in range(n+1):
        dist=location[i]-now
        if dist>b: return False
        if energy-dist<0:
            energy=b
            count+=1
        now=location[i]
        energy-=dist
            
    return count<=k
    
L,n,k=map(int,input().split())
location=list(map(int,input().split()))
location.append(L)
print(sol())