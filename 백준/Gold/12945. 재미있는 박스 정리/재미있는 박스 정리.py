import sys
input=sys.stdin.readline

n=int(input())
number=sorted([int(input()) for i in range(n)])
l=0
r=n//2
cnt=0
while l<n//2 and r<n:
    if number[l]*2<=number[r]:
        cnt+=1
        l+=1
    r+=1
print(n-cnt)