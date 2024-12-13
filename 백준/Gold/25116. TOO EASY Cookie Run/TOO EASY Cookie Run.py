import sys
input=sys.stdin.readline

def sol():
    l=-1
    r=m
    while l+1<r:
        mid=(l+r)//2
        if check(mid):r=mid
        else: l=mid
    return r

def check(mid):
    l=0
    r=0
    count=0
    while r+1<n:
        r+=1
        while number[r]-number[l]+(r-l)*mid>=m:
            count+=n-r
            l+=1
    return count>=k
        
n,m,k=map(int,input().split())
number=[0]+list(map(int,input().split()))
n+=1
for i in range(1,n):
    number[i]+=number[i-1]
print(sol())