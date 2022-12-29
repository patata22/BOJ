import sys
input=sys.stdin.readline

n,m=map(int,input().split())
T=[int(input()) for i in range(n)]
l,r=1,min(T)*m

while l+1<r:
    mid=(l+r)//2
    count=0
    for t in T: count+=mid//t
    if count>=m: r= mid
    else: l= mid
print(r)
        
