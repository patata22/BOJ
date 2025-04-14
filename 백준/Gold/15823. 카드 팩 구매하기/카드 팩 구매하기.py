import sys
input=sys.stdin.readline

def sol():
    l=0
    r=(n//m)+1
    while l+1<r:
        mid=(l+r)//2
        if check(mid): l=mid
        else: r=mid
    return l

def check(mid):
    count={}
    result=0
    l=0
    r=-1
    while r+1<n:
        r+=1
        if number[r] not in count: count[number[r]]=0
        count[number[r]]+=1
        while count[number[r]]>1:
            count[number[l]]-=1
            l+=1
        if r-l+1==mid:
            result+=1
            l=r+1
            r=l-1
            count={}
    return result>=m
        
n,m=map(int,input().split())
number=tuple(map(int,input().split()))

print(sol())
