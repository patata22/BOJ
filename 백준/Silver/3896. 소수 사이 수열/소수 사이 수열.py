import sys
input=sys.stdin.readline

def sol(x):
    l=0
    r=100001
    while l+1<r:
        mid=(l+r)//2
        if prime[mid]>=x: r=mid
        else: l= mid
    left=prime[l]
    l=0
    r=100001
    while l+1<r:
        mid=(l+r)//2
        if prime[mid]<x: l=mid
        else: r=mid
    right=prime[r]
    return right-left


prime=[]
isPrime=[1]*1300000
for i in range(2,1300000):
    if isPrime[i]:
        prime.append(i)
        for j in range(i+i,1300000,i):
            isPrime[j]=0


for tt in range(int(input())):
    n=int(input())
    if isPrime[n]:print(0)
    else:print(sol(n))
        
