import sys
input=sys.stdin.readline

def sol():
    l=max(number)-1
    r=1000000000
    while l+1<r:
        mid=(l+r)//2
        count=0
        now=0
        for x in number:
            if now<x:
                count+=1
                now=mid-x
            else: now-=x
        if count<=m: r=mid
        else: l=mid
    return r
        

n,m=map(int,input().split())
number=[int(input()) for i in range(n)]

print(sol())
