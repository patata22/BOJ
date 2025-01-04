import sys,heapq
input=sys.stdin.readline

def sol():
    l=0
    r=n+1
    while l+1<r:
        mid=(l+r)//2
        if check(mid): r=mid
        else:l=mid
    return r

def check(mid):
    q=[]
    for i in range(mid):
        heapq.heappush(q,number[i])
    idx=mid-1
    while idx+1<n:
        idx+=1
        heapq.heappush(q,heapq.heappop(q)+number[idx])
        
    while len(q)>1:
        heapq.heappop(q)
    return heapq.heappop(q)<=t
        
n,t=map(int,input().split())
number=[int(input()) for i in range(n)]
print(sol())
