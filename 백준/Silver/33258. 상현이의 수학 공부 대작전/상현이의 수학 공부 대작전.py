def sol():
    l=0
    r=10**9
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else: l=mid
    return r

def check(mid):
    result=0
    for x in number:
        if mid>=x: result+=mid
        else: result+=2*(mid-x)
    return result>=L

n=int(input())
number=tuple(map(int,input().split()))
L=int(input())

print(sol())