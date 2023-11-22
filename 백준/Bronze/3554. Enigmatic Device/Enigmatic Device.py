import sys
input=sys.stdin.readline
n=int(input())

number=list(map(int,input().split()))
for _ in range(int(input())):
    c,l,r=map(int,input().split())
    if c==1:
        for i in range(l-1,r):
            number[i]=number[i]**2%2010
    else:
        total=0
        for i in range(l-1,r):
            total+=number[i]
        print(total)
