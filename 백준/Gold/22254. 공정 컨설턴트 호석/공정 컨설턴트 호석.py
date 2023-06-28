import heapq

def sol():
    l=0
    r=n+1
    while l+1<r:
        mid=(l+r)//2
        if check(mid):
            r=mid
        else: l=mid
    return r

def check(mid):
    machine=[0]*mid
    for time in number:
        now=heapq.heappop(machine)
        if time+now>x:return False
        else:
            heapq.heappush(machine,time+now)
    return True

n,x=map(int,input().split())
number=list(map(int,input().split()))

print(sol())
