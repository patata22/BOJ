def work(mid):
    now=0
    for day in number:
        if day-now<mid:
            return False
        now+=mid
    return True

def sol():
    l=1
    r=max(number)+1
    while l+1<r:
        mid=(l+r)//2
        now=0
        if work(mid): l=mid
        else: r=mid

    return l
        

n=int(input())
number=list(map(int,input().split()))
number.sort()
print(sol())
