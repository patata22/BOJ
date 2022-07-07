import sys
input=sys.stdin.readline

def check(x):
    l=-1
    r=n
    while l+1<r:
        mid=(l+r)//2
        if number[mid]==x:return 1
        if number[mid]>x:r=mid
        else:l=mid
    return 0

n=int(input())
number=list(map(int,input().split()))
number.sort()
input()
for x in list(map(int,input().split())):
    print(check(x), end=' ')
