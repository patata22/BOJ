import sys
input=sys.stdin.readline

def binary_left(x):
    l=-1
    r=n
    while l+1<r:
        mid=(l+r)//2
        if big[mid]>=x:
            r=mid
        else: l=mid
    return r

def binary_right(x):
    l=-1
    r=n
    while l+1<r:
        mid=(l+r)//2
        if small[mid]>x:
            r=mid
        else: l=mid
    return r


n=int(input())

original=[]
big=[]
small=[]

for _ in range(n):
    a,b=map(int,input().split())
    original.append((a,b))

for a,b in original:
    big.append(a+b)
    small.append(a-b)

big.sort()
small.sort()

for a,b in original:
    print(binary_left(a-b)+1,binary_right(a+b))

