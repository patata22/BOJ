import sys
input=sys.stdin.readline

n,k=map(int,input().split())
number=sorted(list(map(int,input().split())))
for _ in range(k):
    l,r,x=map(int,input().split())
    for i in range(l-1,r):
        number[i]+=x
    number.sort()
print(*number)
