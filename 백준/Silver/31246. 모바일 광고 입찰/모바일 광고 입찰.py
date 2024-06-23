import sys
input=sys.stdin.readline

def sol():
    l=-1
    r=10**9
    while l+1<r:
        mid=(l+r)//2
        count=0
        for a,b in paper:
            if a+mid>=b: count+=1
        if count>=k: r=mid
        else: l=mid
    return r

n,k=map(int,input().split())
paper=[tuple(map(int,input().split())) for i in range(n)]
print(sol())
