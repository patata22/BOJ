import sys,bisect
input=sys.stdin.readline

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
    print(bisect.bisect_left(big,a-b)+1,bisect.bisect_right(small,a+b))

